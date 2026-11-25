#!/usr/bin/env python3
"""Manuale HACCP semplificato per ristoranti (IT), modelo GRATIS — lead magnet de /it/blog/manuale-haccp-semplificato.

Un solo origen de textos (CONTENUTO) y dos renderizadores, para que el Word y el PDF digan lo mismo:
  - astro-site/public/descargas/manuale-haccp-semplificato-ristorante-aichef.docx — Word editable: estilos reales
    (Titolo, Heading 1/2, «Nota di guida», «Cella»), índice como campo TOC PRE-RELLENADO con las 7 entradas
    (enlaces a marcadores de cada H1, visible en cualquier visor) + `w:updateFields` en settings.xml para que Word
    añada los números de página al abrir, tablas editables con cabecera repetida, A4 con la sección 4 en apaisado,
    pie con PAGE/NUMPAGES, idioma it-IT, core.xml con fecha real y sin la miniatura en blanco de la plantilla.
  - astro-site/public/descargas/manuale-haccp-semplificato-ristorante-aichef.pdf — para imprimir: Arial incrustada
    (signo menos real en «−18 °C» y casillas ☐ con Arial Unicode; en Linux, Liberation Sans + DejaVu Sans), índice con
    páginas, marcadores, pie «Pagina N di M», texto ≥ 9 pt, palabras nunca partidas (se comprueba celda a celda).
Estructura (spec-manuale-it.md): 0 Come usare questo modello · 1 Dati dell’impresa e responsabile del piano ·
2 Descrizione dell’attività · 3 Procedure di base (12 schede «Cosa faccio / Chi / Ogni quanto / Cosa registro») ·
4 Analisi dei pericoli (tabla de 6 columnas, «Limite» = «da definire nel tuo piano») · 5 Registrazioni (5 moduli) ·
6 Verifica e revisione.
Hechos: SOLO los de la ficha reference_normativa-italiana-alergenos-haccp (memoria del proyecto). Ninguna cifra de
temperatura salvo −18 °C (D.Lgs. 110/1992); el DPR 327/1980 solo con «vigenza discussa»; sanciones fuera del modelo
(van en el post). `/descargas/*` está en noindex (netlify.toml). Sesión Claude Code, 25-nov-2026.
"""
import re
import sys
import warnings
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DOCX = RAIZ / 'astro-site/public/descargas/manuale-haccp-semplificato-ristorante-aichef.docx'
PDF = RAIZ / 'astro-site/public/descargas/manuale-haccp-semplificato-ristorante-aichef.pdf'
GUIDA = 'https://aichef.pro/it/blog/manuale-haccp-semplificato'
TABELLA_ALLERGENI = 'https://aichef.pro/it/blog/lista-allergeni-alimentari'

NERO, ORO, GRIGIO_TESTO, GRIGIO_NOTA, FONDO, BORDO = '111111', 'FFD700', '555555', '666666', 'F3F3F3', 'A8A8A8'
NB = ' '
CASELLA = '☐'  # ☐

# ================================================================ Testi (unica fonte per Word e PDF)
TITOLO = 'Manuale HACCP semplificato per ristoranti'
TITOLO_RIGHE = ('Manuale HACCP semplificato', 'per ristoranti')
SOTTOTITOLO = 'Modello di piano di autocontrollo semplificato da compilare'
BADGE = 'Modello gratuito · non è un modello ufficiale'
PIEDE = f'Modello gratuito di AI Chef Pro · non è un modello ufficiale · Guida: {GUIDA}'
NOTA_COPERTINA = ('Le note in corsivo grigio ti guidano nella compilazione: nella versione Word puoi cancellarle. '
                  'Verifica sempre le indicazioni della tua Regione e della tua ASL.')
TOC_NOTA = ('In Word, se l’indice non mostra i numeri di pagina, fai clic con il tasto destro sull’indice e scegli '
            '«Aggiorna campo».')
DATA_DOCUMENTO = (2026, 11, 25)  # docProps/core.xml: creazione e ultima modifica
CAMPI_COPERTINA = [('Ragione sociale', 1), ('Insegna del locale', 1), ('Indirizzo del locale', 1),
                   ('Responsabile del piano', 1), ('Data di stesura', 1), ('Revisione n. e data', 1)]
SEGNAPOSTO = 'da definire nel tuo piano'

TITOLI = ['0. Come usare questo modello',
          '1. Dati dell’impresa e responsabile del piano',
          '2. Descrizione dell’attività',
          '3. Procedure di base (prerequisiti)',
          '4. Analisi dei pericoli e misure di controllo',
          '5. Registrazioni',
          '6. Verifica e revisione']


class Ph(str):
    """Testo segnaposto in una cella (corsivo grigio): il compilatore lo sostituisce con il suo valore."""


def H1(i, nuova=True):
    return ('h1', TITOLI[i], nuova)


def H2(t):
    return ('h2', t)


def G(t):
    return ('g', t)


def P(t):
    return ('p', t)


def L(*voci):
    return ('l', list(voci))


def SOTTO(t):
    return ('sotto', t)


def CAMPI(*righe):
    return ('campi', list(righe))


def CAMPI2(*righe):
    """Campi su 4 colonne: ogni riga ha uno (a tutta larghezza) o due campi «etichetta | valore»."""
    assert all(len(r) in (1, 2) for r in righe)
    return ('campi2', [list(r) for r in righe])


def SCELTE(*righe):
    return ('scelte', list(righe))


def TAB(testata, larghezze, righe=(), vuote=0, alt=8.0, unita=False):
    assert abs(sum(larghezze) - 1) < 1e-6, larghezze
    assert all(len(r) == len(testata) for r in righe), testata
    return ('tab', dict(testata=testata, larghezze=larghezze, righe=[list(r) for r in righe], vuote=vuote, alt=alt,
                        unita=unita))


def BOX(etichetta, alt):
    return ('box', etichetta, alt)


def ORIENT(o):
    return ('orient', o)


def GRUPPO(*blocchi):
    return ('gruppo', list(blocchi))


SCHEDA_ETICHETTE = ('Cosa faccio', 'Chi', 'Ogni quanto', 'Cosa registro')
ALTEZZE_SCHEDA = (17, 8, 9)
FRAZIONI_CAMPI2 = (0.2, 0.3, 0.2, 0.3)  # mm: Cosa faccio · Chi / Ogni quanto · Cosa registro


def SCHEDA(titolo, guida, *extra):
    return GRUPPO(H2(titolo), G(guida), ('scheda',), *extra)


ALLERGENI_URL = TABELLA_ALLERGENI.replace('https://', '')

SEZ_0 = [
    H1(0),
    G('Leggi questa pagina prima di iniziare: ti aiuta a capire se la versione semplificata fa per te e come '
      'compilarla.'),
    P('In Italia non c’è una legge nazionale sul manuale HACCP semplificato e non esiste un modello ufficiale. La '
      'possibilità di semplificare nasce dalla flessibilità prevista dal Reg. (CE) 852/2004 e dalla Comunicazione '
      'della Commissione 2022/C 355/01; chi può usarla, e a quali condizioni, lo stabiliscono la tua Regione o la tua ASL. Due '
      'esempi:'),
    L('<b>Piemonte</b> (D.D. 359/2024): imprese fino a 5 addetti, oppure fino a 10 se la ASL le ritiene idonee;',
      '<b>Emilia-Romagna</b> (DGR 1869/2008): imprese fino a 10 addetti.'),
    P('Nelle altre Regioni verifica le linee guida regionali o chiedi alla tua ASL prima di adottare la versione '
      'semplificata.'),
    P('<b>Non è un modello ufficiale.</b> È un modello gratuito di AI Chef Pro: adattalo alla tua attività e alle '
      'regole della tua Regione.'),
    P('<b>Chi lo compila.</b> Il piano lo scrivi tu, come operatore del settore alimentare (OSA), anche con l’aiuto '
      'di un consulente: non serve la firma di un tecnico.'),
    P('<b>Dove lo conservi.</b> Il piano va tenuto a disposizione dell’autorità di controllo, anche in formato '
      'digitale.'),
    P('<b>Come si compila.</b> Riempi i campi e le tabelle. Tieni solo le schede pertinenti alla tua attività, '
      'aggiungi quelle che mancano e adatta le righe di esempio ai tuoi piatti. I limiti di temperatura li fissi tu: '
      'il modello non ne precompila nessuno, tranne −18 °C per i surgelati.'),
]

SEZ_1 = [
    H1(1, nuova=False),
    G('Indica chi sei e chi è responsabile del piano di autocontrollo: di solito il titolare o una persona '
      'incaricata dal titolare.'),
    GRUPPO(SOTTO('Impresa'),
           CAMPI2([('Ragione sociale', 1)], [('Insegna del locale', 1), ('Partita IVA', 1)], [('Sede legale', 1)],
                  [('Sede del locale (se diversa)', 1)], [('Telefono', 1), ('E-mail', 1)],
                  [('Attività svolta', 1), ('Numero di addetti', 1)])),
    GRUPPO(SOTTO('Responsabile del piano di autocontrollo'),
           CAMPI2([('Nome e cognome', 1), ('Ruolo nell’impresa', 1)], [('Formazione (corso, ente, data)', 2)],
                  [('Consulente che ha collaborato (se c’è)', 1)],
                  [('Data di prima stesura', 1), ('Revisione n. e data', 1)], [('Firma del responsabile', 1.5)])),
]

SEZ_2 = [
    H1(2, nuova=False),
    G('Descrivi in poche righe cosa fai e per chi: è la base per l’analisi dei pericoli della sezione 4.'),
    CAMPI(('Tipo di locale (ristorante, trattoria, pizzeria, agriturismo, bar con cucina…)', 1),
          ('Numero di coperti', 1), ('Giorni e orari di apertura', 1),
          ('Piatti e preparazioni principali', 3),
          ('Preparazioni fatte in anticipo (cotture, raffreddamento, conservazione, riscaldamento)', 2)),
    SOTTO('Servizio e consumatori'),
    SCELTE(('Servizio', ['al tavolo', 'asporto', 'consegna a domicilio', 'catering ed eventi']),
           ('Servi abitualmente gruppi vulnerabili (per esempio in una mensa per bambini, anziani o malati)?',
            ['sì', 'no']),
           ('Prepari piatti dichiarati «senza allergeni»?', ['sì', 'no']),
           ('Produci conserve?', ['sì', 'no']),
           ('Servi pesce crudo o poco cotto?', ['sì', 'no'])),
    P('<b>Attenzione:</b> secondo la Comunicazione 2022/C 355/01, se prepari alimenti per gruppi vulnerabili, piatti '
      'dichiarati «senza allergeni» o conserve, l’analisi dei pericoli va fatta per intero anche in un locale '
      'piccolo: chiedi alla tua ASL che cosa puoi semplificare. Se servi pesce crudo o poco cotto, vedi la scheda '
      '3.2.'),
]

LIMITI_37 = TAB(['Cosa controllo', 'Limite (fissato da te)', 'Come lo misuro', 'Ogni quanto'],
                [0.30, 0.28, 0.24, 0.18],
                [['Frigoriferi (prodotti refrigerati)', Ph(SEGNAPOSTO), '', ''],
                 ['Surgelati acquistati', '−18 °C o meno (D.Lgs. 110/1992)', '', ''],
                 ['Alimenti congelati da te', Ph(SEGNAPOSTO), '', ''],
                 ['Cottura', Ph(SEGNAPOSTO), '', ''],
                 ['Raffreddamento', Ph(SEGNAPOSTO), '', ''],
                 ['Mantenimento a caldo', Ph(SEGNAPOSTO), '', ''],
                 ['Riscaldamento', Ph(SEGNAPOSTO), '', ''],
                 ['Bonifica anti-Anisakis (se la fai tu)', 'tempi e temperature del Reg. (CE) 853/2004', '', '']],
                vuote=1, alt=8.5, unita=True)

SEZ_3 = [
    H1(3),
    G('Le procedure di base sono le buone prassi igieniche su cui si regge tutto il piano. In ogni scheda scrivi '
      'cosa fai, chi lo fa, ogni quanto e cosa registri. Tieni solo le schede pertinenti alla tua attività e '
      'aggiungi quelle che mancano.'),
    SCHEDA('3.1 Locali e attrezzature (manutenzione)',
           'Descrivi come tieni in buono stato locali, impianti e attrezzature (frigoriferi, forni, piani di lavoro, '
           'lavelli) e a chi ti rivolgi in caso di guasto. Annota gli interventi di manutenzione.'),
    SCHEDA('3.2 Materie prime e fornitori (ricevimento)',
           'Indica come scegli i fornitori e cosa controlli quando arriva la merce: integrità delle confezioni, '
           'etichetta, data di scadenza e temperatura dei prodotti refrigerati e surgelati (i limiti sono quelli '
           'della scheda 3.7). Se servi pesce o cefalopodi crudi o poco cotti (anche marinati), devono aver subito la '
           'bonifica anti-Anisakis, salvo le esenzioni previste (Reg. (CE) 853/2004, allegato III, sezione VIII): se '
           'la fa il fornitore, conserva la sua attestazione; se la fai tu, descrivila nella scheda 3.7.'),
    SCHEDA('3.3 Rifiuti',
           'Indica dove raccogli i rifiuti (contenitori chiudibili, lontani dagli alimenti), ogni quanto li svuoti e '
           'chi li ritira, compresi gli oli di frittura esausti.'),
    SCHEDA('3.4 Infestanti',
           'Disegna nel riquadro la pianta del locale con la posizione delle esche (oppure allegala) e annota ogni '
           'avvistamento nel registro della sezione 5. Se ti affidi a una ditta specializzata, indica il nome e '
           'conserva i rapporti di intervento.',
           BOX('Pianta del locale con la posizione delle esche', 56)),
    SCHEDA('3.5 Pulizia e sanificazione',
           'Il dettaglio (cosa pulisci, con quale prodotto, ogni quanto e chi lo fa) va nel piano di pulizia della '
           'sezione 5. La verifica può essere visiva: prima di iniziare a lavorare controlla che superfici e attrezzature siano '
           'pulite. Conserva le schede tecniche di detergenti e disinfettanti.'),
    SCHEDA('3.6 Acqua',
           'Se usi l’acqua della rete pubblica, conserva il contratto o l’ultima bolletta. Se usi un pozzo o '
           'un’altra fonte privata, chiedi alla tua ASL quali controlli servono.'),
    GRUPPO(H2('3.7 Temperature'),
           G('Catena del freddo, cottura, raffreddamento, mantenimento a caldo e riscaldamento: i limiti li fissi tu '
             'nel piano e li motivi con l’analisi dei pericoli della sezione 4. Il modello non precompila nessuna '
             'cifra, tranne quella dei surgelati: −18 °C o meno (D.Lgs. 110/1992). Molti manuali riportano i valori '
             'del DPR 327/1980, abrogato dal D.Lgs. 27/2021 con una clausola di salvaguardia: la loro vigenza è '
             'discussa, quindi il valore che scegli va scritto e motivato nel tuo piano.'),
           ('scheda',)),
    GRUPPO(SOTTO('I limiti del mio piano'), LIMITI_37),
    SCHEDA('3.8 Allergeni',
           'Tieni una documentazione scritta degli allergeni presenti in ogni piatto, facilmente consultabile dal '
           'cliente e dall’autorità di controllo (art. 19, comma 8, D.Lgs. 231/2017): l’informazione solo a voce non '
           'basta. Attrezzature e contenitori usati per lavorare, manipolare, trasportare o conservare un allergene '
           'si usano per alimenti che non lo contengono solo dopo averli puliti e controllati, almeno per verificare '
           'che non restino residui visibili (Reg. (CE) 852/2004, allegato II, capitolo IX, punto 9). Per la '
           f'documentazione puoi usare la nostra tabella allergeni gratuita: <a href="{TABELLA_ALLERGENI}">'
           f'{ALLERGENI_URL}</a>.'),
    SCHEDA('3.9 Igiene e salute del personale',
           'Indica le regole per chi lavora in cucina e in sala: abiti da lavoro puliti, mani lavate spesso, unghie '
           'corte e niente anelli o bracciali durante le preparazioni. Chi ha disturbi come diarrea, vomito o febbre, '
           'o ferite infette, lo comunica al responsabile e non manipola alimenti.'),
    SCHEDA('3.10 Formazione',
           'Chi manipola alimenti deve essere formato, e chi prepara e aggiorna le procedure deve avere una '
           'formazione adeguata sui principi HACCP (Reg. (CE) 852/2004, allegato II, capitolo XII). Non esiste un '
           'attestato HACCP nazionale: durata dei corsi, '
           'aggiornamenti e chi li organizza dipendono dalla tua Regione (in Lombardia e in Emilia-Romagna, per '
           'esempio, la formazione è responsabilità dell’operatore). Annota i corsi nel registro della sezione 5.'),
    SCHEDA('3.11 Rintracciabilità e ritiro/richiamo',
           'Conserva fatture e documenti di trasporto (DDT) per sapere da chi hai comprato ogni prodotto. Se un '
           'fornitore o l’autorità ritira o richiama un prodotto, toglilo subito dall’uso, separalo con un cartello '
           '«non utilizzare» e segui le istruzioni ricevute. Se sei tu a sospettare che un alimento che hai servito '
           'o venduto non sia sicuro, ritiralo e informa subito la ASL (art. 19 Reg. (CE) 178/2002).'),
    SCHEDA('3.12 Materiali a contatto con gli alimenti (MOCA)',
           'Usa solo materiali e oggetti adatti al contatto con gli alimenti (lo indicano l’etichetta, il simbolo del '
           'bicchiere e della forchetta o il fornitore), conserva le dichiarazioni di conformità che ti consegnano i '
           'fornitori e sostituisci taglieri e contenitori rovinati.'),
]

PH = Ph(SEGNAPOSTO)
ANALISI = TAB(['Fase', 'Pericolo', 'Misura di controllo', 'Limite (fissato da te)', 'Come lo controllo',
               'Azione correttiva'],
              [0.12, 0.17, 0.21, 0.14, 0.17, 0.19],
              [['Ricevimento', 'Prodotti alterati, scaduti o non alla temperatura giusta; confezioni rotte',
                'Fornitori di fiducia; controllo della merce all’arrivo', PH,
                'Controllo a vista di etichetta e scadenza; termometro per refrigerati e surgelati',
                'Respingo la merce o la separo, avviso il fornitore e annoto la non conformità'],
               ['Conservazione a freddo', 'Moltiplicazione di batteri; contaminazione tra crudi e cotti',
                'Frigoriferi e congelatori alla temperatura del piano (surgelati a −18 °C o meno); alimenti coperti '
                'ed etichettati, crudi separati dai cotti', PH, 'Termometro del frigorifero; controllo a vista',
                'Sposto i prodotti in un altro frigorifero, valuto se sono ancora sicuri e chiamo il tecnico'],
               ['Preparazione', 'Contaminazione crociata (tra crudi e cotti, da allergeni); mani o superfici sporche',
                'Mani lavate; superfici e utensili puliti tra un uso e l’altro; alimenti fuori dal frigorifero solo '
                'per il tempo necessario', PH, 'A vista',
                'Scarto l’alimento contaminato, pulisco di nuovo e ricordo le regole al personale'],
               ['Cottura', 'Batteri che sopravvivono a una cottura insufficiente', 'Cottura completa, secondo la ricetta',
                PH, 'Termometro a sonda o a vista (colore, consistenza, liquidi di cottura)', 'Prolungo la cottura'],
               ['Raffreddamento', 'Moltiplicazione dei batteri sopravvissuti alla cottura, se il raffreddamento è lento',
                'Raffreddamento rapido (abbattitore, porzioni piccole, contenitori bassi), poi in frigorifero', PH,
                'Termometro a sonda e orario', 'Se il raffreddamento non rispetta il piano, scarto l’alimento'],
               ['Mantenimento a caldo', 'Moltiplicazione di batteri se la temperatura scende',
                'Banco caldo o bagnomaria alla temperatura del piano, per un tempo limitato', PH, 'Termometro a sonda',
                'Riscaldo o scarto, come previsto dal piano'],
               ['Riscaldamento', 'Batteri che sopravvivono a un riscaldamento insufficiente',
                'Riscaldamento completo, fino al cuore del prodotto, e una sola volta', PH,
                'Termometro a sonda o a vista (fumante in tutta la massa)', 'Prolungo il riscaldamento'],
               ['Servizio', 'Contaminazione durante il servizio; informazione sbagliata sugli allergeni',
                'Piatti protetti; personale che conosce gli allergeni di ogni piatto', PH,
                'A vista; documentazione allergeni aggiornata',
                'Ritiro il piatto, lo rifaccio e do al cliente l’informazione corretta']],
              vuote=10, alt=11)
FASI = [r[0] for r in ANALISI[1]['righe']]

SEZ_4 = [
    ORIENT('orizzontale'),
    H1(4, nuova=False),
    G('Per ogni fase indica il pericolo, come lo tieni sotto controllo, il limite che fissi tu, come lo controlli e '
      'cosa fai se qualcosa va storto. Le righe sono un esempio: adattale ai tuoi piatti, cancella quelle che non ti '
      'servono e aggiungine altre.'),
    P('La colonna «Limite» è vuota di proposito: il limite lo fissi tu e lo motivi nel piano. Se una fase è un punto '
      'critico di controllo (CCP), scrivi «CCP» accanto al nome della fase. La Comunicazione 2022/C 355/01 riconosce '
      'che in un ristorante friggere o grigliare «potrebbe non essere un CCP», perché la temperatura dell’olio o del '
      'grasso si vede facilmente: quel pericolo si può tenere sotto controllo con le buone prassi igieniche della '
      'sezione 3.'),
    ANALISI,
]

PULIZIA_AREE = ['Piani di lavoro', 'Taglieri e utensili', 'Affettatrice (se c’è)', 'Frigoriferi e congelatori',
                'Forno e piano cottura', 'Friggitrice', 'Cappa e filtri', 'Lavelli', 'Lavastoviglie', 'Pavimenti',
                'Pareti e porte', 'Spogliatoio e servizi igienici del personale', 'Contenitori dei rifiuti']
NOTA_REGISTRAZIONI = ('Dove la tua Regione lo ammette (per esempio in Piemonte), puoi registrare solo le non '
                      'conformità e le azioni correttive. La Comunicazione 2022/C 355/01 lo spiega così: «mantenere '
                      'la temperatura corretta è di gran lunga più importante che registrarla».')

SEZ_5 = [
    ORIENT('verticale'),
    H1(5, nuova=False),
    G('Qui trovi i moduli da compilare al computer o da stampare: fai tutte le copie che ti servono, aggiungi righe '
      'quando mancano e conserva i moduli compilati insieme al piano.'),
    GRUPPO(H2('5.1 Non conformità e azioni correttive'),
           G('Annota ogni volta che qualcosa non va (un frigorifero sopra il limite del piano, merce respinta, un '
             'errore sugli allergeni) e cosa hai fatto per rimediare.'),
           P(NOTA_REGISTRAZIONI),
           TAB(['Data', 'Cosa è successo', 'Azione correttiva', 'Chi', 'Firma'], [0.12, 0.33, 0.33, 0.11, 0.11],
               vuote=11, alt=10)),
    GRUPPO(H2('5.2 Registro della formazione'),
           G('Annota i corsi e gli aggiornamenti di chi lavora con te, secondo le regole della tua Regione, e conserva '
             'gli attestati.'),
           TAB(['Data', 'Nome e cognome', 'Mansione', 'Corso o argomento', 'Ente o docente', 'Firma'],
               [0.11, 0.20, 0.14, 0.25, 0.18, 0.12], vuote=6, alt=9)),
    GRUPPO(H2('5.3 Elenco dei fornitori'),
           G('Elenca i fornitori con i prodotti che ti consegnano: ti serve per la rintracciabilità (scheda 3.11). '
             'Nelle note indica i documenti che conservi, per esempio l’attestazione della bonifica anti-Anisakis.'),
           TAB(['Fornitore', 'Prodotti forniti', 'Contatti (indirizzo, telefono)', 'Note e documenti'],
               [0.24, 0.26, 0.26, 0.24], vuote=6, alt=10)),
    GRUPPO(H2('5.4 Piano di pulizia'),
           G('Per ogni area o attrezzatura indica cosa pulisci, con quale prodotto e dosaggio, ogni quanto e chi lo '
             'fa. La verifica può essere visiva.'),
           TAB(['Area o attrezzatura', 'Cosa pulisco', 'Prodotto e dosaggio', 'Ogni quanto', 'Chi'],
               [0.27, 0.25, 0.22, 0.14, 0.12], [[a, '', '', '', ''] for a in PULIZIA_AREE], vuote=2, alt=8)),
    GRUPPO(H2('5.5 Registro degli avvistamenti di infestanti'),
           G('Annota ogni avvistamento di insetti, roditori o loro tracce e cosa hai fatto. La pianta con la posizione '
             'delle esche è nella scheda 3.4.'),
           TAB(['Data', 'Dove', 'Cosa è stato visto', 'Azione correttiva', 'Chi / firma'],
               [0.12, 0.18, 0.26, 0.30, 0.14], vuote=6, alt=9.5)),
]

SEZ_6 = [
    H1(6, nuova=False),
    G('Il piano funziona solo se resta aggiornato: controlla che le procedure si applichino davvero e rivedilo quando '
      'cambia qualcosa.'),
    P('<b>Verifica.</b> Ogni tanto controlla che le procedure vengano applicate: osserva il lavoro in cucina e in sala '
      'e rileggi le registrazioni delle non conformità per capire se qualche problema si ripete.'),
    P('<b>Quando rivedere il piano:</b>'),
    L('quando aggiungi un nuovo piatto o una nuova preparazione;',
      'quando cambi fornitore o ne aggiungi uno nuovo;',
      'quando installi una nuova attrezzatura o modifichi i locali;',
      'dopo una non conformità, se una procedura va corretta.'),
    P('Come buona prassi, rileggilo almeno una volta l’anno anche se non è cambiato nulla.'),
    TAB(['Revisione n.', 'Data', 'Motivo', 'Cosa è cambiato', 'Firma del responsabile'],
        [0.13, 0.12, 0.25, 0.32, 0.18], [['1', '', 'Prima stesura', '', '']], vuote=6, alt=10),
]

CONTENUTO = SEZ_0 + SEZ_1 + SEZ_2 + SEZ_3 + SEZ_4 + SEZ_5 + SEZ_6
H2_ATTESI = ['3.%d' % i for i in range(1, 13)] + ['5.%d' % i for i in range(1, 6)]

# Note chiave che entrambi i file devono contenere (testo normalizzato: spazi unificatori → spazi)
NOTE_CHIAVE = ['Piemonte', 'D.D. 359/2024', 'Emilia-Romagna', 'DGR 1869/2008', '2022/C 355/01', 'D.Lgs. 231/2017',
               'D.Lgs. 110/1992', '−18 °C', SEGNAPOSTO, 'non è un modello ufficiale', 'potrebbe non essere un CCP',
               'è di gran lunga più importante che registrarla', 'allegato II, capitolo IX, punto 9',
               'contratto o l’ultima bolletta', 'vigenza è discussa', 'Modello gratuito di AI Chef Pro',
               'aichef.pro/it/blog/manuale-haccp-semplificato', 'aichef.pro/it/blog/lista-allergeni-alimentari',
               'non serve la firma di un tecnico', 'anche in formato digitale', 'bonifica anti-Anisakis',
               'Cosa faccio', 'Ogni quanto', 'Cosa registro', 'Azione correttiva', 'Limite (fissato da te)',
               'almeno una volta l’anno',
               # arreglos de la auditoría jurídica del PR #284
               'va fatta per intero', 'la tua Regione o la tua ASL', 'cefalopodi', 'salvo le esenzioni previste',
               '178/2002', 'informa subito la ASL', 'capitolo XII', 'formazione adeguata sui principi HACCP',
               'Affettatrice (se c’è)', 'si vede facilmente']


# ================================================================ Tipografia
_NB_DOPO = re.compile(r'(?<![\w.])(art\.|comma|D\.Lgs\.|D\.D\.|DGR|DPR|Reg\.|\(CE\)|\(UE\)|allegato|capitolo|punto|'
                      r'sezione|scheda|n\.|L\.R\.) (?=[\dIVX(])')


def it(s):
    """Spazio unificatore dopo «art.», «D.Lgs.», «Reg.», «(CE)», «allegato»… davanti al numero; «−18 °C»; «2022/C 355/01»."""
    s = _NB_DOPO.sub(r'\1' + NB, s)
    s = re.sub(r'(\d) °C', r'\1' + NB + '°C', s)
    return s.replace('2022/C 355/01', '2022/C' + NB + '355/01')


def piano(s):
    """Testo senza markup, per i controlli."""
    s = re.sub(r'<[^>]+>', '', s)
    return s


def normalizza(s):
    return ' '.join(s.replace(NB, ' ').replace(' ', ' ').split())


# ================================================================ Word (.docx)
def genera_docx():
    from docx import Document
    from docx.enum.section import WD_ORIENT, WD_SECTION
    from docx.enum.style import WD_STYLE_TYPE
    from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_ROW_HEIGHT_RULE, WD_TABLE_ALIGNMENT
    from docx.enum.text import WD_TAB_ALIGNMENT, WD_TAB_LEADER
    from docx.opc.constants import RELATIONSHIP_TYPE as RT
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Emu, Mm, Pt, RGBColor

    FONT = 'Arial'

    def rgb(h):
        return RGBColor.from_string(h)

    def imposta_font(rPr, nome=FONT):
        rf = rPr.find(qn('w:rFonts'))
        if rf is None:
            rf = OxmlElement('w:rFonts')
            rPr.insert(0, rf)
        for a in ('w:asciiTheme', 'w:hAnsiTheme', 'w:eastAsiaTheme', 'w:cstheme'):
            rf.attrib.pop(qn(a), None)
        for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'):
            rf.set(qn(a), nome)

    def imposta_colore(stile, h):
        stile.font.color.rgb = rgb(h)
        c = stile.element.rPr.find(qn('w:color'))
        assert c is not None and c.get(qn('w:themeColor')) is None

    PPR_DOPO_PBDR = ('w:shd', 'w:tabs', 'w:suppressAutoHyphens', 'w:kinsoku', 'w:wordWrap', 'w:overflowPunct',
                     'w:topLinePunct', 'w:autoSpaceDE', 'w:autoSpaceDN', 'w:bidi', 'w:adjustRightInd', 'w:snapToGrid',
                     'w:spacing', 'w:ind', 'w:contextualSpacing', 'w:mirrorIndents', 'w:suppressOverlap', 'w:jc',
                     'w:textDirection', 'w:textAlignment', 'w:textboxTightWrap', 'w:outlineLvl', 'w:divId',
                     'w:cnfStyle', 'w:rPr', 'w:sectPr', 'w:pPrChange')

    def bordo_paragrafo(pPr, lato, colore, sz):
        vecchio = pPr.find(qn('w:pBdr'))
        if vecchio is not None:
            pPr.remove(vecchio)
        pBdr = OxmlElement('w:pBdr')
        b = OxmlElement('w:' + lato)
        for k, v in (('w:val', 'single'), ('w:sz', str(sz)), ('w:space', '4'), ('w:color', colore)):
            b.set(qn(k), v)
        pBdr.append(b)
        pPr.insert_element_before(pBdr, *PPR_DOPO_PBDR)

    doc = Document()
    stili = doc.styles

    # --- docDefaults: Arial, lingua italiana (controllo ortografico)
    rpr_def = stili.element.find(qn('w:docDefaults')).find(qn('w:rPrDefault')).find(qn('w:rPr'))
    imposta_font(rpr_def)
    lang = rpr_def.find(qn('w:lang'))
    if lang is None:
        lang = OxmlElement('w:lang')
        rpr_def.append(lang)
    lang.set(qn('w:val'), 'it-IT')
    lang.set(qn('w:eastAsia'), 'it-IT')

    normale = stili['Normal']
    imposta_font(normale.element.get_or_add_rPr())
    normale.font.size = Pt(10)
    imposta_colore(normale, NERO)
    normale.paragraph_format.space_after = Pt(5)
    normale.paragraph_format.line_spacing = 1.12

    for nome, dim, prima, dopo in (('Heading 1', 15, 14, 8), ('Heading 2', 12, 12, 3)):
        s = stili[nome]
        rPr = s.element.get_or_add_rPr()
        imposta_font(rPr)
        imposta_colore(s, NERO)
        s.font.size = Pt(dim)
        s.font.bold = True
        s.font.italic = False
        s.paragraph_format.space_before = Pt(prima)
        s.paragraph_format.space_after = Pt(dopo)
        s.paragraph_format.keep_with_next = True
    bordo_paragrafo(stili['Heading 1'].element.get_or_add_pPr(), 'bottom', ORO, 8)

    titolo = stili['Title']
    rPr = titolo.element.get_or_add_rPr()
    imposta_font(rPr)
    imposta_colore(titolo, NERO)
    for tag in ('w:spacing', 'w:kern'):
        e = rPr.find(qn(tag))
        if e is not None:
            rPr.remove(e)
    titolo.font.size = Pt(26)
    titolo.font.bold = True
    titolo.paragraph_format.space_after = Pt(10)
    bordo_paragrafo(titolo.element.get_or_add_pPr(), 'bottom', ORO, 12)

    def nuovo_stile(nome, base='Normal', dim=10, corsivo=False, grassetto=False, colore=NERO, dopo=5, prima=0,
                    interl=1.12, kwn=False):
        s = stili.add_style(nome, WD_STYLE_TYPE.PARAGRAPH)
        s.base_style = stili[base]
        s.quick_style = True
        rPr = s.element.get_or_add_rPr()
        imposta_font(rPr)
        imposta_colore(s, colore)
        s.font.size = Pt(dim)
        s.font.italic = corsivo
        s.font.bold = grassetto
        pf = s.paragraph_format
        pf.space_after, pf.space_before, pf.line_spacing, pf.keep_with_next = Pt(dopo), Pt(prima), interl, kwn
        return s

    nuovo_stile('Sottotitolo modello', dim=13, colore='444444', dopo=14)
    nuovo_stile('Nota di guida', dim=9.5, corsivo=True, colore=GRIGIO_NOTA, dopo=6, kwn=True)
    nuovo_stile('Etichetta di gruppo', dim=10.5, grassetto=True, dopo=3, prima=6, kwn=True)
    nuovo_stile('Cella', dim=9.5, dopo=1, prima=1, interl=1.0)
    nuovo_stile('Cella intestazione', base='Cella', grassetto=True)
    nuovo_stile('Piè di pagina modello', dim=8.5, colore=GRIGIO_TESTO, dopo=0, interl=1.0)
    lb = stili['List Bullet']
    imposta_font(lb.element.get_or_add_rPr())
    lb.font.size = Pt(10)
    lb.paragraph_format.space_after = Pt(3)
    toc1 = nuovo_stile('toc 1', dim=10.5, dopo=3)  # nome e id dello stile integrato di Word per l'indice
    toc1.element.attrib.pop(qn('w:customStyle'), None)
    toc1.element.styleId = 'TOC1'
    toc1.paragraph_format.tab_stops.add_tab_stop(Mm(170), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)

    # --- Pagina A4
    sez = doc.sections[0]
    sez.page_width, sez.page_height = Mm(210), Mm(297)
    sez.left_margin = sez.right_margin = Mm(20)
    sez.top_margin, sez.bottom_margin = Mm(18), Mm(22)
    sez.header_distance, sez.footer_distance = Mm(10), Mm(9)

    def larghezza_testo():
        s = doc.sections[-1]
        return (s.page_width - s.left_margin - s.right_margin) / 36000  # EMU → mm

    # --- Run, link, campi
    TOKEN = re.compile(r'(<b>|</b>|<a href="[^"]+">|</a>)')

    def run_semplice(par, testo, grassetto=None, corsivo=None, colore=None, dim=None):
        # ☐ con un font che ha il glifo
        for pezzo in re.split('(%s)' % CASELLA, testo):
            if not pezzo:
                continue
            r = par.add_run(pezzo)
            if grassetto:
                r.bold = True
            if corsivo:
                r.italic = True
            if colore:
                r.font.color.rgb = rgb(colore)
            if dim:
                r.font.size = Pt(dim)
            if pezzo == CASELLA:
                rPr = r._r.get_or_add_rPr()
                imposta_font(rPr, 'Segoe UI Symbol')
        return par

    def aggiungi_link(par, url, testo, dim=None, colore='1A5FB4'):
        r_id = par.part.relate_to(url, RT.HYPERLINK, is_external=True)
        h = OxmlElement('w:hyperlink')
        h.set(qn('r:id'), r_id)
        r = OxmlElement('w:r')
        rPr = OxmlElement('w:rPr')
        c = OxmlElement('w:color')
        c.set(qn('w:val'), colore)
        u = OxmlElement('w:u')
        u.set(qn('w:val'), 'single')
        rPr.append(c)
        if dim:
            sz = OxmlElement('w:sz')
            sz.set(qn('w:val'), str(int(dim * 2)))
            rPr.append(sz)
        rPr.append(u)
        r.append(rPr)
        t = OxmlElement('w:t')
        t.text = testo
        t.set(qn('xml:space'), 'preserve')
        r.append(t)
        h.append(r)
        par._p.append(h)

    def scrivi(par, testo, corsivo=None, colore=None, dim=None):
        testo = it(testo)
        grassetto, href = False, None
        for pezzo in TOKEN.split(testo):
            if pezzo == '<b>':
                grassetto = True
            elif pezzo == '</b>':
                grassetto = False
            elif pezzo.startswith('<a href='):
                href = pezzo.split('"')[1]
            elif pezzo == '</a>':
                href = None
            elif pezzo:
                if href:
                    aggiungi_link(par, href, pezzo, dim=dim)
                else:
                    run_semplice(par, pezzo, grassetto=grassetto, corsivo=corsivo, colore=colore, dim=dim)
        return par

    def campo(par, istruzione, risultato):
        def fld(tipo):
            r = OxmlElement('w:r')
            f = OxmlElement('w:fldChar')
            f.set(qn('w:fldCharType'), tipo)
            r.append(f)
            return r
        par._p.append(fld('begin'))
        r = OxmlElement('w:r')
        it_ = OxmlElement('w:instrText')
        it_.set(qn('xml:space'), 'preserve')
        it_.text = ' %s ' % istruzione
        r.append(it_)
        par._p.append(r)
        par._p.append(fld('separate'))
        run_semplice(par, risultato)
        par._p.append(fld('end'))

    # --- Tabelle
    TCPR_DOPO_SHD = ('w:noWrap', 'w:tcMar', 'w:textDirection', 'w:tcFitText', 'w:vAlign', 'w:hideMark',
                     'w:headers', 'w:cellIns', 'w:cellDel', 'w:cellMerge', 'w:tcPrChange')
    TCPR_DOPO_BORDI = ('w:shd',) + TCPR_DOPO_SHD

    def sfondo(cella, colore):
        tcPr = cella._tc.get_or_add_tcPr()
        shd = OxmlElement('w:shd')
        shd.set(qn('w:val'), 'clear')
        shd.set(qn('w:color'), 'auto')
        shd.set(qn('w:fill'), colore)
        tcPr.insert_element_before(shd, *TCPR_DOPO_SHD)

    def bordo_sotto(cella, colore=NERO, sz=8):
        tcPr = cella._tc.get_or_add_tcPr()
        b = OxmlElement('w:tcBorders')
        e = OxmlElement('w:bottom')
        for k, v in (('w:val', 'single'), ('w:sz', str(sz)), ('w:space', '0'), ('w:color', colore)):
            e.set(qn(k), v)
        b.append(e)
        tcPr.insert_element_before(b, *TCPR_DOPO_BORDI)

    def riga_pr(riga):
        """La riga non si spezza tra due pagine."""
        trPr = riga._tr.get_or_add_trPr()
        cs = OxmlElement('w:cantSplit')
        trPr.insert_element_before(cs, 'w:trHeight', 'w:tblHeader', 'w:tblCellSpacing', 'w:jc', 'w:hidden',
                                   'w:ins', 'w:del', 'w:trPrChange')

    def nuova_tabella(n_righe, larghezze_mm, unita=False):
        t = doc.add_table(rows=n_righe, cols=len(larghezze_mm))
        t.alignment = WD_TABLE_ALIGNMENT.LEFT
        t.autofit = False
        tblPr = t._tbl.tblPr
        bordi = OxmlElement('w:tblBorders')
        for lato in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
            e = OxmlElement('w:' + lato)
            for k, v in (('w:val', 'single'), ('w:sz', '4'), ('w:space', '0'), ('w:color', BORDO)):
                e.set(qn(k), v)
            bordi.append(e)
        tblPr.insert_element_before(bordi, 'w:shd', 'w:tblLayout', 'w:tblCellMar', 'w:tblLook', 'w:tblCaption',
                                    'w:tblDescription')
        tblW = tblPr.find(qn('w:tblW'))
        if tblW is None:
            tblW = OxmlElement('w:tblW')
            tblPr.insert_element_before(tblW, 'w:jc', 'w:tblCellSpacing', 'w:tblInd', 'w:tblBorders', 'w:shd',
                                        'w:tblLayout', 'w:tblCellMar', 'w:tblLook')
        tblW.set(qn('w:type'), 'dxa')
        tblW.set(qn('w:w'), str(int(round(sum(larghezze_mm) / 25.4 * 1440))))
        for i, w in enumerate(larghezze_mm):
            t.columns[i].width = Mm(w)
        for r in t.rows:
            for i, c in enumerate(r.cells):
                c.width = Mm(larghezze_mm[i])
                c.paragraphs[0].style = stili['Cella']
        for i, r in enumerate(t.rows):
            riga_pr(r)
            if unita and i < len(t.rows) - 1:  # la tabella resta su una pagina
                for c in r.cells:
                    c.paragraphs[0].paragraph_format.keep_with_next = True
        return t

    def scrivi_cella(cella, testo, intestazione=False, etichetta=False):
        par = cella.paragraphs[0]
        if intestazione or etichetta:
            par.style = stili['Cella intestazione']
            sfondo(cella, FONDO)
            cella.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
        if isinstance(testo, Ph):
            scrivi(par, testo, corsivo=True, colore='777777')
        elif testo:
            scrivi(par, testo)

    def altezza(riga, mm):
        riga.height = Mm(mm)
        riga.height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST

    def spaziatore():
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.line_spacing = Pt(7)

    def tabella_campi(righe, frazioni=(0.34, 0.66), unita=True):
        W = larghezza_testo()
        t = nuova_tabella(len(righe), [W * f for f in frazioni], unita=unita)
        for r, (etichetta, n) in zip(t.rows, righe):
            scrivi_cella(r.cells[0], etichetta, etichetta=True)
            altezza(r, 8 * n)
        spaziatore()
        return t

    def unisci(riga, da, a):
        c = riga.cells[da].merge(riga.cells[a])
        for p in c.paragraphs[1:]:  # dopo la fusione restano paragrafi vuoti in più
            p._p.getparent().remove(p._p)
        c.paragraphs[0].style = stili['Cella']
        return c

    def tabella_campi2(righe):
        W = larghezza_testo()
        t = nuova_tabella(len(righe), [W * f for f in FRAZIONI_CAMPI2], unita=True)
        for r, campi in zip(t.rows, righe):
            scrivi_cella(r.cells[0], campi[0][0], etichetta=True)
            if len(campi) == 2:
                scrivi_cella(r.cells[2], campi[1][0], etichetta=True)
            altezza(r, 8 * max(n for _, n in campi))
        for r, campi in zip(t.rows, righe):
            if len(campi) == 1:
                unisci(r, 1, 3)
        spaziatore()

    def tabella_scelte(righe):
        W = larghezza_testo()
        t = nuova_tabella(len(righe), [W * 0.56, W * 0.44], unita=True)
        for r, (domanda, opzioni) in zip(t.rows, righe):
            scrivi_cella(r.cells[0], domanda, etichetta=True)
            scrivi_cella(r.cells[1], '   '.join(CASELLA + ' ' + o for o in opzioni))
            r.cells[1].vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            altezza(r, 8)
        spaziatore()

    def tabella_scheda():
        W = larghezza_testo()
        fr = (0.2, 0.35, 0.17, 0.28)
        t = nuova_tabella(3, [W * f for f in fr], unita=True)
        r0, r1, r2 = t.rows
        a = unisci(r0, 1, 3)
        unisci(r2, 1, 3)
        a.paragraphs[0].paragraph_format.keep_with_next = True
        scrivi_cella(r0.cells[0], SCHEDA_ETICHETTE[0], etichetta=True)
        scrivi_cella(r1.cells[0], SCHEDA_ETICHETTE[1], etichetta=True)
        scrivi_cella(r1.cells[2], SCHEDA_ETICHETTE[2], etichetta=True)
        scrivi_cella(r2.cells[0], SCHEDA_ETICHETTE[3], etichetta=True)
        for r, h in zip((r0, r1, r2), ALTEZZE_SCHEDA):
            altezza(r, h)
        spaziatore()

    def tabella_dati(spec):
        W = larghezza_testo()
        righe = spec['righe'] + [[''] * len(spec['testata'])] * spec['vuote']
        t = nuova_tabella(1 + len(righe), [W * f for f in spec['larghezze']], unita=spec['unita'])
        intest = t.rows[0]
        riga_pr_th = intest._tr.get_or_add_trPr()
        th = OxmlElement('w:tblHeader')
        riga_pr_th.insert_element_before(th, 'w:tblCellSpacing', 'w:jc', 'w:hidden', 'w:ins', 'w:del',
                                         'w:trPrChange')
        for c, testo in zip(intest.cells, spec['testata']):
            scrivi_cella(c, testo, intestazione=True)
            bordo_sotto(c)
        for r, valori in zip(t.rows[1:], righe):
            for c, v in zip(r.cells, valori):
                scrivi_cella(c, v)
            altezza(r, spec['alt'])
        spaziatore()

    def tabella_box(etichetta, alt):
        W = larghezza_testo()
        t = nuova_tabella(2, [W], unita=True)
        scrivi_cella(t.rows[0].cells[0], etichetta, etichetta=True)
        altezza(t.rows[1], alt)
        spaziatore()

    # --- Indice: campo TOC con il risultato già scritto (7 voci che portano al titolo), così non è vuoto in nessun
    #     visore; Word lo rigenera con i numeri di pagina all'apertura (w:updateFields in settings.xml).
    def segnalibro(par, i):
        nome = '_Toc_sez%d' % i
        bs = OxmlElement('w:bookmarkStart')
        bs.set(qn('w:id'), str(100 + i))
        bs.set(qn('w:name'), nome)
        be = OxmlElement('w:bookmarkEnd')
        be.set(qn('w:id'), str(100 + i))
        pPr = par._p.pPr
        if pPr is not None:
            pPr.addnext(bs)
        else:
            par._p.insert(0, bs)
        par._p.append(be)

    def fld_run(tipo):
        r = OxmlElement('w:r')
        f = OxmlElement('w:fldChar')
        f.set(qn('w:fldCharType'), tipo)
        r.append(f)
        return r

    def indice_precompilato():
        for i, titolo in enumerate(TITOLI):
            par = doc.add_paragraph(style=stili['toc 1'])
            if i == 0:
                par._p.append(fld_run('begin'))
                r = OxmlElement('w:r')
                istr = OxmlElement('w:instrText')
                istr.set(qn('xml:space'), 'preserve')
                istr.text = ' TOC \\o "1-1" \\h \\z \\u '
                r.append(istr)
                par._p.append(r)
                par._p.append(fld_run('separate'))
            h = OxmlElement('w:hyperlink')
            h.set(qn('w:anchor'), '_Toc_sez%d' % i)
            h.set(qn('w:history'), '1')
            r = OxmlElement('w:r')
            t = OxmlElement('w:t')
            t.text = it(titolo)
            t.set(qn('xml:space'), 'preserve')
            r.append(t)
            h.append(r)
            par._p.append(h)
            if i == len(TITOLI) - 1:
                par._p.append(fld_run('end'))

    # --- Copertina
    p = doc.add_paragraph(style=stili['Etichetta di gruppo'])
    p.paragraph_format.space_before = Pt(40)
    run_semplice(p, 'AI Chef Pro', colore=GRIGIO_TESTO)
    p = doc.add_paragraph(TITOLO_RIGHE[0], style=stili['Title'])
    p.add_run().add_break()
    p.add_run(TITOLO_RIGHE[1])
    doc.add_paragraph(SOTTOTITOLO, style=stili['Sottotitolo modello'])
    p = doc.add_paragraph(style=stili['Etichetta di gruppo'])
    run_semplice(p, BADGE)
    p.paragraph_format.space_after = Pt(18)
    tabella_campi(CAMPI_COPERTINA, frazioni=(0.32, 0.68))
    p = doc.add_paragraph('Indice', style=stili['Etichetta di gruppo'])
    p.paragraph_format.space_before = Pt(14)
    indice_precompilato()
    p = doc.add_paragraph(style=stili['Nota di guida'])
    scrivi(p, TOC_NOTA)
    p = doc.add_paragraph(style=stili['Nota di guida'])
    p.paragraph_format.space_before = Pt(18)
    scrivi(p, NOTA_COPERTINA)

    # --- Corpo
    def rendi(b):
        tipo = b[0]
        if tipo == 'h1':
            p = doc.add_paragraph(it(b[1]), style=stili['Heading 1'])
            p.paragraph_format.page_break_before = b[2]
            segnalibro(p, TITOLI.index(b[1]))
        elif tipo == 'h2':
            doc.add_paragraph(it(b[1]), style=stili['Heading 2'])
        elif tipo == 'g':
            scrivi(doc.add_paragraph(style=stili['Nota di guida']), b[1])
        elif tipo == 'p':
            scrivi(doc.add_paragraph(style=stili['Normal']), b[1])
        elif tipo == 'sotto':
            scrivi(doc.add_paragraph(style=stili['Etichetta di gruppo']), b[1])
        elif tipo == 'l':
            for v in b[1]:
                scrivi(doc.add_paragraph(style=stili['List Bullet']), v)
        elif tipo == 'campi':
            tabella_campi(b[1])
        elif tipo == 'campi2':
            tabella_campi2(b[1])
        elif tipo == 'scelte':
            tabella_scelte(b[1])
        elif tipo == 'scheda':
            tabella_scheda()
        elif tipo == 'tab':
            tabella_dati(b[1])
        elif tipo == 'box':
            tabella_box(b[1], b[2])
        elif tipo == 'orient':
            s = doc.add_section(WD_SECTION.NEW_PAGE)
            if b[1] == 'orizzontale':
                s.orientation = WD_ORIENT.LANDSCAPE
                s.page_width, s.page_height = Mm(297), Mm(210)
            else:
                s.orientation = WD_ORIENT.PORTRAIT
                s.page_width, s.page_height = Mm(210), Mm(297)
        elif tipo == 'gruppo':
            for x in b[1]:
                rendi(x)
        else:
            raise ValueError(tipo)

    for b in CONTENUTO:
        rendi(b)

    # --- Piè di pagina (uno per sezione, con la tabulazione a destra della sua larghezza)
    for s in doc.sections:
        f = s.footer
        f.is_linked_to_previous = False
        p1 = f.paragraphs[0]
        p1.style = stili['Piè di pagina modello']
        bordo_paragrafo(p1._p.get_or_add_pPr(), 'top', ORO, 6)
        run_semplice(p1, 'Modello gratuito di AI Chef Pro · non è un modello ufficiale · Guida: ')
        aggiungi_link(p1, GUIDA, GUIDA, dim=8.5)
        p2 = f.add_paragraph(style=stili['Piè di pagina modello'])
        larg = (s.page_width - s.left_margin - s.right_margin)
        p2.paragraph_format.tab_stops.add_tab_stop(Emu(larg), WD_TAB_ALIGNMENT.RIGHT)
        run_semplice(p2, '\tPagina ')
        campo(p2, 'PAGE', '1')
        run_semplice(p2, ' di ')
        campo(p2, 'NUMPAGES', '1')

    cp = doc.core_properties
    cp.title, cp.author, cp.subject = TITOLO, 'AI Chef Pro', BADGE
    cp.language, cp.keywords = 'it-IT', 'manuale HACCP semplificato, piano di autocontrollo, ristorante'
    cp.comments = 'Modello gratuito. Guida: ' + GUIDA
    from datetime import datetime
    cp.created = cp.modified = datetime(*DATA_DOCUMENTO, 9, 0, 0)
    cp.last_modified_by, cp.revision = 'AI Chef Pro', 1

    # Word aggiorna i campi (indice con i numeri di pagina) all'apertura
    impost = doc.settings.element
    uf = OxmlElement('w:updateFields')
    uf.set(qn('w:val'), 'true')
    impost.insert_element_before(uf, 'w:hdrShapeDefaults', 'w:footnotePr', 'w:endnotePr', 'w:compat', 'w:docVars',
                                 'w:rsids')
    # via la miniatura bianca della plantilla di python-docx
    pkg = doc.part.package
    for rId, rel in list(pkg.rels.items()):
        if rel.reltype.endswith('/metadata/thumbnail'):
            del pkg.rels[rId]
            pkg.rels.related_parts.pop(rId, None)
    DOCX.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(DOCX))


# ================================================================ PDF
def trova_font():
    """Arial (macOS) o Liberation Sans (Linux) per il testo; Arial Unicode o DejaVu Sans per la casella ☐."""
    cand = {
        'Testo': ['/System/Library/Fonts/Supplemental/Arial.ttf', '/Library/Fonts/Arial.ttf',
                  '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf',
                  '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
                  '/usr/share/fonts/liberation-sans/LiberationSans-Regular.ttf'],
        'Testo-Bold': ['/System/Library/Fonts/Supplemental/Arial Bold.ttf', '/Library/Fonts/Arial Bold.ttf',
                       '/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf',
                       '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
                       '/usr/share/fonts/liberation-sans/LiberationSans-Bold.ttf'],
        'Testo-Italic': ['/System/Library/Fonts/Supplemental/Arial Italic.ttf', '/Library/Fonts/Arial Italic.ttf',
                         '/usr/share/fonts/truetype/msttcorefonts/Arial_Italic.ttf',
                         '/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf',
                         '/usr/share/fonts/liberation-sans/LiberationSans-Italic.ttf'],
        'Testo-BoldItalic': ['/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf',
                             '/Library/Fonts/Arial Bold Italic.ttf',
                             '/usr/share/fonts/truetype/msttcorefonts/Arial_Bold_Italic.ttf',
                             '/usr/share/fonts/truetype/liberation/LiberationSans-BoldItalic.ttf',
                             '/usr/share/fonts/liberation-sans/LiberationSans-BoldItalic.ttf'],
        'Simboli': ['/System/Library/Fonts/Supplemental/Arial Unicode.ttf', '/Library/Fonts/Arial Unicode.ttf',
                    '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', '/usr/share/fonts/dejavu/DejaVuSans.ttf'],
    }
    trovati = {}
    for nome, percorsi in cand.items():
        for p in percorsi:
            if Path(p).exists():
                trovati[nome] = p
                break
        else:
            sys.exit(f'Font non trovato per {nome}: {percorsi}')
    return trovati


def genera_pdf():
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.pdfmetrics import registerFont, registerFontFamily, stringWidth
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import (BaseDocTemplate, Frame, HRFlowable, KeepTogether, NextPageTemplate, PageBreak,
                                    PageTemplate, Paragraph, Spacer, Table, TableStyle)
    from reportlab.platypus.tableofcontents import TableOfContents

    font = trova_font()
    for nome, p in font.items():
        registerFont(TTFont(nome, p))
    registerFontFamily('Testo', normal='Testo', bold='Testo-Bold', italic='Testo-Italic', boldItalic='Testo-BoldItalic')
    for nome in ('Testo', 'Testo-Italic'):
        f = pdfmetrics.getFont(nome).face.charToGlyph
        assert 0x2212 in f and 0x2019 in f and 0xab in f, nome
    assert 0x2610 in pdfmetrics.getFont('Simboli').face.charToGlyph

    C = lambda h: colors.HexColor('#' + h)  # noqa: E731
    MX, MT, MB = 20 * mm, 18 * mm, 24 * mm
    DIM_MIN = 9

    stili = {}

    def st(nome, **kw):
        base = dict(fontName='Testo', fontSize=10, leading=13.5, textColor=C(NERO), splitLongWords=0)
        base.update(kw)
        assert base['fontSize'] >= DIM_MIN, nome
        stili[nome] = ParagraphStyle(nome, **base)
        return stili[nome]

    st('Corpo', spaceAfter=5)
    st('Guida', fontName='Testo-Italic', fontSize=9.5, leading=12.5, textColor=C(GRIGIO_NOTA), spaceAfter=6)
    st('H1', fontName='Testo-Bold', fontSize=15, leading=18, spaceBefore=12, spaceAfter=2, keepWithNext=1)
    st('H2', fontName='Testo-Bold', fontSize=12, leading=15, spaceBefore=9, spaceAfter=3, keepWithNext=1)
    st('Sotto', fontName='Testo-Bold', fontSize=10.5, leading=13, spaceBefore=6, spaceAfter=3, keepWithNext=1)
    st('Punto', leftIndent=14, bulletIndent=3, spaceAfter=3, bulletFontName='Testo', bulletFontSize=10)
    st('Cella', fontSize=9, leading=11.3)
    st('CellaB', fontName='Testo-Bold', fontSize=9, leading=11.3)
    st('CellaPh', fontName='Testo-Italic', fontSize=9, leading=11.3, textColor=C('777777'))
    st('Marchio', fontName='Testo-Bold', fontSize=10.5, leading=13, textColor=C(GRIGIO_TESTO), spaceAfter=6)
    st('Titolo', fontName='Testo-Bold', fontSize=26, leading=31, spaceAfter=4)
    st('Sottotitolo', fontSize=13, leading=17, textColor=C('444444'), spaceBefore=8, spaceAfter=8)
    st('Badge', fontName='Testo-Bold', fontSize=11, leading=14, spaceAfter=16)
    st('Toc0', fontSize=10.5, leading=17)

    def t(s):
        s = it(s)
        s = re.sub(r'<a href="([^"]+)">', r'<a href="\1" color="#1a5fb4">', s)
        return s.replace(CASELLA, '<font name="Simboli">%s</font>' % CASELLA)

    controlli = {'celle': 0}

    def controlla_parole(testo, stile, larghezza):
        """Nessuna parola (o gruppo unito da spazi unificatori) più larga dello spazio disponibile: non si spezza."""
        pulito = piano(it(testo))
        for parola in pulito.split():
            nome = stile.fontName
            w = stringWidth(parola.replace(CASELLA, 'M'), nome, stile.fontSize)
            assert w <= larghezza + 0.01, (parola, round(w, 1), round(larghezza, 1))

    def par(testo, stile, larghezza):
        controlla_parole(testo, stile, larghezza)
        return Paragraph(t(testo), stile)

    PAD = 4

    def tabella(righe_celle, larghezze, min_alt, testata=False, stile_extra=(), spans=()):
        """righe_celle: liste di (testo, stile) o None; altezza = max(minimo, contenuto)."""
        dati, alt = [], []
        span_coperte = set()
        for (c0, r0), (c1, r1) in spans:
            for rr in range(r0, r1 + 1):
                for cc in range(c0, c1 + 1):
                    if (cc, rr) != (c0, r0):
                        span_coperte.add((cc, rr))
        for ri, (riga, h_min) in enumerate(zip(righe_celle, min_alt)):
            celle, h = [], h_min
            for ci, x in enumerate(riga):
                if x is None or (ci, ri) in span_coperte:
                    celle.append('')
                    continue
                testo, stile = x
                larg = larghezze[ci]
                for (c0, r0), (c1, r1) in spans:
                    if (c0, r0) == (ci, ri):
                        larg = sum(larghezze[c0:c1 + 1])
                p = par(testo, stile, larg - 2 * PAD)
                controlli['celle'] += 1
                h = max(h, p.wrap(larg - 2 * PAD, 10000)[1] + 2 * 3.2)
                celle.append(p)
            dati.append(celle)
            alt.append(h)
        tab = Table(dati, colWidths=larghezze, rowHeights=alt, repeatRows=1 if testata else 0, hAlign='LEFT')
        stile = [('GRID', (0, 0), (-1, -1), 0.5, C(BORDO)), ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                 ('LEFTPADDING', (0, 0), (-1, -1), PAD), ('RIGHTPADDING', (0, 0), (-1, -1), PAD),
                 ('TOPPADDING', (0, 0), (-1, -1), 3), ('BOTTOMPADDING', (0, 0), (-1, -1), 3)]
        if testata:
            stile += [('BACKGROUND', (0, 0), (-1, 0), C(FONDO)), ('LINEBELOW', (0, 0), (-1, 0), 1, C(NERO)),
                      ('VALIGN', (0, 0), (-1, 0), 'MIDDLE')]
        for s in spans:
            stile.append(('SPAN',) + s)
        tab.setStyle(TableStyle(stile + list(stile_extra)))
        return tab

    stato = {'W': A4[0] - 2 * MX}

    def campi(righe, frazioni=(0.34, 0.66)):
        W = stato['W']
        lw = [W * f for f in frazioni]
        return tabella([[(e, stili['CellaB']), None] for e, _ in righe], lw, [8 * mm * n for _, n in righe],
                       stile_extra=[('BACKGROUND', (0, 0), (0, -1), C(FONDO)), ('VALIGN', (0, 0), (0, -1), 'MIDDLE')])

    def campi2(righe):
        W = stato['W']
        lw = [W * f for f in FRAZIONI_CAMPI2]
        B = stili['CellaB']
        dati_, spans, extra = [], [], []
        for i, campi in enumerate(righe):
            if len(campi) == 2:
                dati_.append([(campi[0][0], B), None, (campi[1][0], B), None])
                extra += [('BACKGROUND', (2, i), (2, i), C(FONDO)), ('VALIGN', (2, i), (2, i), 'MIDDLE')]
            else:
                dati_.append([(campi[0][0], B), None, None, None])
                spans.append(((1, i), (3, i)))
        return tabella(dati_, lw, [8 * mm * max(n for _, n in c) for c in righe], spans=spans,
                       stile_extra=[('BACKGROUND', (0, 0), (0, -1), C(FONDO)), ('VALIGN', (0, 0), (0, -1), 'MIDDLE')]
                       + extra)

    def scelte(righe):
        W = stato['W']
        lw = [W * 0.56, W * 0.44]
        sep = NB + NB + NB + ' '
        return tabella([[(d, stili['CellaB']), (sep.join(CASELLA + NB + o for o in opz), stili['Cella'])]
                        for d, opz in righe], lw, [8 * mm] * len(righe),
                       stile_extra=[('BACKGROUND', (0, 0), (0, -1), C(FONDO)), ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')])

    def scheda():
        W = stato['W']
        lw = [W * f for f in (0.2, 0.35, 0.17, 0.28)]
        e = SCHEDA_ETICHETTE
        B = stili['CellaB']
        return tabella([[(e[0], B), None, None, None], [(e[1], B), None, (e[2], B), None], [(e[3], B), None, None, None]],
                       lw, [h * mm for h in ALTEZZE_SCHEDA], spans=[((1, 0), (3, 0)), ((1, 2), (3, 2))],
                       stile_extra=[('BACKGROUND', (0, 0), (0, -1), C(FONDO)), ('BACKGROUND', (2, 1), (2, 1), C(FONDO)),
                                    ('VALIGN', (0, 0), (0, -1), 'MIDDLE'), ('VALIGN', (2, 1), (2, 1), 'MIDDLE')])

    def dati(spec):
        W = stato['W']
        lw = [W * f for f in spec['larghezze']]
        righe = [[(h, stili['CellaB']) for h in spec['testata']]]
        for r in spec['righe']:
            righe.append([None if not v else (v, stili['CellaPh'] if isinstance(v, Ph) else stili['Cella'])
                          for v in r])
        righe += [[None] * len(spec['testata'])] * spec['vuote']
        return tabella(righe, lw, [0] + [spec['alt'] * mm] * (len(righe) - 1), testata=True)

    def box(etichetta, alt):
        W = stato['W']
        return tabella([[(etichetta, stili['CellaB'])], [None]], [W], [0, alt * mm],
                       stile_extra=[('BACKGROUND', (0, 0), (0, 0), C(FONDO))])

    def rendi(b):
        tipo = b[0]
        W = stato['W']
        if tipo == 'h1':
            out = [PageBreak()] if b[2] else []
            h = par(b[1], stili['H1'], W)
            hr = HRFlowable(width='100%', thickness=1, color=C(ORO), spaceBefore=1, spaceAfter=7)
            hr.keepWithNext = 1
            return out + [h, hr]
        if tipo == 'h2':
            return [par(b[1], stili['H2'], W)]
        if tipo == 'g':
            p = par(b[1], stili['Guida'], W)
            p.keepWithNext = 1
            return [p]
        if tipo == 'p':
            return [par(b[1], stili['Corpo'], W)]
        if tipo == 'sotto':
            return [par(b[1], stili['Sotto'], W)]
        if tipo == 'l':
            out = []
            for v in b[1]:
                controlla_parole(v, stili['Punto'], W - 14)
                out.append(Paragraph(t(v), stili['Punto'], bulletText='•'))
            return out
        if tipo == 'campi':
            return [campi(b[1]), Spacer(1, 5)]
        if tipo == 'campi2':
            return [campi2(b[1]), Spacer(1, 5)]
        if tipo == 'scelte':
            return [scelte(b[1]), Spacer(1, 5)]
        if tipo == 'scheda':
            return [scheda(), Spacer(1, 4)]
        if tipo == 'tab':
            return [dati(b[1]), Spacer(1, 6)]
        if tipo == 'box':
            return [box(b[1], b[2]), Spacer(1, 4)]
        if tipo == 'orient':
            stato['W'] = (landscape(A4)[0] if b[1] == 'orizzontale' else A4[0]) - 2 * MX
            return [NextPageTemplate(b[1]), PageBreak()]
        if tipo == 'gruppo':
            interno = []
            for x in b[1]:
                interno += rendi(x)
            return [KeepTogether(interno)]
        raise ValueError(tipo)

    def piede(canv, doc):
        """Piè di pagina: il totale delle pagine viene dal passaggio precedente di multiBuild (il gate lo verifica)."""
        larg, _ = canv._pagesize
        canv.saveState()
        canv.setStrokeColor(C(ORO))
        canv.setLineWidth(0.8)
        canv.line(MX, 17.5 * mm, larg - MX, 17.5 * mm)
        canv.setFillColor(C(GRIGIO_TESTO))
        canv.setFont('Testo', 9)
        assert stringWidth(PIEDE, 'Testo', 9) <= larg - 2 * MX
        canv.drawString(MX, 13 * mm, PIEDE)
        x0 = MX + stringWidth(PIEDE[:PIEDE.index('https')], 'Testo', 9)
        canv.linkURL(GUIDA, (x0, 12 * mm, x0 + stringWidth(GUIDA, 'Testo', 9), 16 * mm), relative=0)
        canv.drawRightString(larg - MX, 8.5 * mm, f'Pagina {doc.page} di {doc.totale or "?"}')
        canv.restoreState()

    class Documento(BaseDocTemplate):
        def __init__(self, percorso, **kw):
            BaseDocTemplate.__init__(self, percorso, pagesize=A4, leftMargin=MX, rightMargin=MX, topMargin=MT,
                                     bottomMargin=MB, **kw)
            v, o = A4, landscape(A4)
            fv = Frame(MX, MB, v[0] - 2 * MX, v[1] - MT - MB, id='fv', leftPadding=0, rightPadding=0, topPadding=0,
                       bottomPadding=0)
            fo = Frame(MX, MB, o[0] - 2 * MX, o[1] - MT - MB, id='fo', leftPadding=0, rightPadding=0, topPadding=0,
                       bottomPadding=0)
            self.addPageTemplates([PageTemplate(id='verticale', frames=[fv], pagesize=v, onPage=piede),
                                   PageTemplate(id='orizzontale', frames=[fo], pagesize=o, onPage=piede)])
            self.totale = None

        def build(self, *a, **k):
            BaseDocTemplate.build(self, *a, **k)
            self.totale = self.page

        def afterFlowable(self, f):
            if isinstance(f, Paragraph) and f.style.name == 'H1':
                testo = f.getPlainText()
                chiave = 'sez' + testo[0]
                self.canv.bookmarkPage(chiave)
                self.canv.addOutlineEntry(testo.replace(NB, ' '), chiave, level=0, closed=False)
                self.notify('TOCEntry', (0, testo, self.page, chiave))

    kw = dict(title=TITOLO, author='AI Chef Pro', subject=BADGE, creator='AI Chef Pro',
              keywords='manuale HACCP semplificato, piano di autocontrollo, ristorante')
    try:
        doc = Documento(str(PDF), lang='it-IT', **kw)
    except (TypeError, ValueError):
        doc = Documento(str(PDF), **kw)

    W = stato['W']
    toc = TableOfContents()
    toc.levelStyles = [stili['Toc0']]
    storia = [Spacer(1, 22 * mm), par('AI Chef Pro', stili['Marchio'], W), par('<br/>'.join(TITOLO_RIGHE), stili['Titolo'], W),
              HRFlowable(width='100%', thickness=1.5, color=C(ORO), spaceBefore=2, spaceAfter=4),
              par(SOTTOTITOLO, stili['Sottotitolo'], W), par(BADGE, stili['Badge'], W),
              campi(CAMPI_COPERTINA, frazioni=(0.32, 0.68)), Spacer(1, 12),
              par('Indice', stili['Sotto'], W), toc, Spacer(1, 14), par(NOTA_COPERTINA, stili['Guida'], W)]
    for b in CONTENUTO:
        storia += rendi(b)
    PDF.parent.mkdir(parents=True, exist_ok=True)
    doc.multiBuild(storia)
    return controlli['celle']


# ================================================================ Gate
SPAGNOLO = {'el', 'los', 'las', 'y', 'que', 'por', 'para', 'como', 'pero', 'también', 'fecha', 'limpieza',
            'proveedor', 'proveedores', 'alimentos', 'cocina', 'plato', 'platos', 'número', 'página', 'es', 'son',
            'está', 'hay', 'debe', 'puede', 'hora', 'semana', 'año', 'mes', 'nombre', 'responsable', 'temperaturas', 'alérgenos', 'controles', 'registros', 'medidas', 'peligro', 'acción'}
INGLESE = {'the', 'and', 'of', 'with', 'for', 'to', 'is', 'are', 'date', 'cleaning', 'supplier', 'suppliers', 'food',
           'page', 'fill', 'template', 'guide', 'download', 'free', 'check', 'by', 'from', 'this', 'that', 'your',
           'you', 'record', 'log', 'staff', 'hazard', 'step', 'limit', 'corrective', 'action', 'signature', 'name',
           'how', 'what', 'who', 'when'}
TEMP = re.compile(r'[−–-]?\s?\d+(?:[.,]\d+)?\s?°\s?C|\d+\s*gradi')


def controlli_testo(testo, dove):
    n = normalizza(testo)
    mancanti = [k for k in NOTE_CHIAVE if k not in n]
    assert not mancanti, (dove, mancanti)
    temp = set(TEMP.findall(n))
    assert temp == {'−18 °C'}, (dove, temp)
    assert not re.search(r'è\s+legge', n), dove
    assert not re.search(r'327/(?:80|1980)[^.]{0,80}(?:vigente|in vigore)', n), dove
    parole = set(re.findall(r'[a-zà-öø-ÿ]+', n.lower()))
    assert not (parole & SPAGNOLO), (dove, parole & SPAGNOLO)
    assert not (parole & INGLESE), (dove, parole & INGLESE)
    assert not re.search('[ñ¿¡áíóúÁÍÓÚ]', n), (dove, re.findall('.{20}[ñ¿¡áíóúÁÍÓÚ].{20}', n))
    for vietato in ('193/2007', 'sanzion', '1.000', '6.000', '60 °C', '65 °C', 'è obbligatorio registrare',
                    'arriva prima una diffida', 'flessibilità non vale', 'flessibilità non si applica',
                    'piccolo ristorante', 'lo stabilisce la tua Regione'):
        assert vietato not in n, (dove, vietato)
    return n


def gate_docx():
    from docx import Document
    from docx.oxml.ns import qn
    from docx.shared import Mm
    with zipfile.ZipFile(DOCX) as z:
        assert z.testzip() is None
        nomi = z.namelist()
        impost = z.read('word/settings.xml').decode('utf-8')
        core = z.read('docProps/core.xml').decode('utf-8')
    assert not any('thumbnail' in x for x in nomi), nomi
    assert '<w:updateFields w:val="true"/>' in impost
    data = '%04d-%02d-%02dT' % DATA_DOCUMENTO
    for tag in ('dcterms:created', 'dcterms:modified'):
        assert re.search('<%s [^>]*>%s' % (tag, data), core), (tag, core)
    assert '<dc:creator>AI Chef Pro</dc:creator>' in core and '<cp:lastModifiedBy>AI Chef Pro<' in core, core
    d = Document(str(DOCX))
    # indice: 7 voci dentro il campo TOC, ognuna collegata al segnalibro del suo titolo
    voci = [p for p in d.paragraphs if p.style.name == 'toc 1']
    assert [normalizza(''.join(x.text or '' for x in p._p.iter(qn('w:t')))) for p in voci] == \
        [normalizza(x) for x in TITOLI], [p._p.xml[:200] for p in voci]
    segnalibri = {b.get(qn('w:name')) for b in d.element.body.iter(qn('w:bookmarkStart'))}
    ancore = [h.get(qn('w:anchor')) for p in voci for h in p._p.iter(qn('w:hyperlink'))]
    assert len(ancore) == len(TITOLI) and set(ancore) <= segnalibri, (ancore, segnalibri)
    tipi = [f.get(qn('w:fldCharType')) for p in voci for f in p._p.iter(qn('w:fldChar'))]
    assert tipi == ['begin', 'separate', 'end'], tipi
    h1 = [normalizza(p.text) for p in d.paragraphs if p.style.name == 'Heading 1']
    assert h1 == [normalizza(x) for x in TITOLI], h1
    h2 = [normalizza(p.text).split(' ')[0] for p in d.paragraphs if p.style.name == 'Heading 2']
    assert h2 == H2_ATTESI, h2
    guide = sum(1 for p in d.paragraphs if p.style.name == 'Nota di guida')
    assert guide >= len(TITOLI) + len(H2_ATTESI), guide
    # ogni H1 è seguito da una nota di guida
    ps = d.paragraphs
    for i, p in enumerate(ps):
        if p.style.name in ('Heading 1', 'Heading 2'):
            assert ps[i + 1].style.name == 'Nota di guida', p.text
    orient = []
    for s in d.sections:
        w, h = round(s.page_width / 36000), round(s.page_height / 36000)
        assert (w, h) in ((210, 297), (297, 210)), (w, h)
        orient.append('O' if w > h else 'V')
        piede = ' '.join(x.text for x in s.footer._element.iter(qn('w:t')))
        istr = ' '.join(x.text for x in s.footer._element.iter(qn('w:instrText')))
        assert 'non è un modello ufficiale' in piede and GUIDA in piede, piede
        assert 'PAGE' in istr and 'NUMPAGES' in istr, istr
    assert orient == ['V', 'O', 'V'], orient
    assert any('TOC' in (x.text or '') for x in d.element.body.iter(qn('w:instrText')))
    n_tab = len(d.tables)
    # testo completo: paragrafi (anche nelle tabelle e nei link) + piè di pagina
    corpo = []
    for p in d.element.body.iter(qn('w:p')):
        corpo.append(''.join(x.text or '' for x in p.iter(qn('w:t'))))
    for s in d.sections:
        for p in s.footer._element.iter(qn('w:p')):
            corpo.append(''.join(x.text or '' for x in p.iter(qn('w:t'))))
    testo = '\n'.join(corpo)
    n = controlli_testo(testo, 'docx')
    assert n.count(SEGNAPOSTO) == len(FASI) + 6, n.count(SEGNAPOSTO)
    def conta(blocchi, tipo):
        return sum(conta(x[1], tipo) if x[0] == 'gruppo' else int(x[0] == tipo) for x in blocchi)
    n_th = sum(1 for x in d.element.body.iter(qn('w:tblHeader')))
    assert n_th == conta(CONTENUTO, 'tab') == 8, n_th  # una intestazione ripetuta per tabella di dati
    assert n_tab == 1 + sum(conta(CONTENUTO, k) for k in ('tab', 'campi', 'campi2', 'scelte', 'scheda', 'box')), n_tab
    return n_tab


def gate_pdf():
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        from pypdf import PdfReader
        r = PdfReader(str(PDF))
        pagine = len(r.pages)
        assert 6 <= pagine <= 14, f'{pagine} pagine'
        testi = [p.extract_text() for p in r.pages]
        orizz = [i + 1 for i, p in enumerate(r.pages) if float(p.mediabox.width) > float(p.mediabox.height)]
        for p in r.pages:
            assert abs(min(float(p.mediabox.width), float(p.mediabox.height)) - 595.28) < 1
        # dimensione minima del testo: tutti gli operatori Tf dei flussi di contenuto
        dimensioni = set()
        for p in r.pages:
            dati = p.get_contents().get_data().decode('latin-1')
            dimensioni |= {float(x) for x in re.findall(r'/\S+ ([\d.]+) Tf', dati)}
        outline = [o.title for o in r.outline if not isinstance(o, list)]
        meta = r.metadata
    assert dimensioni and min(dimensioni) >= 9, sorted(dimensioni)
    assert outline == [normalizza(x) for x in TITOLI], outline
    assert orizz, 'nessuna pagina orizzontale'
    assert meta.title == TITOLO, meta.title
    tutto = normalizza('\n'.join(testi))
    for titolo in TITOLI:  # indice + titolo nel corpo
        assert tutto.count(normalizza(titolo)) >= 2, titolo
    for h2 in H2_ATTESI:
        assert re.search(r'(?<![\d.])' + re.escape(h2) + r' [A-Z]', tutto), h2
    controlli_testo(tutto, 'pdf')
    for i, tx in enumerate(testi, 1):
        n = normalizza(tx)
        assert PIEDE in n and f'Pagina {i} di {pagine}' in n, (i, n[-200:])
    # la sezione 4 è nelle pagine orizzontali
    pag4 = [i + 1 for i, tx in enumerate(testi) if normalizza(TITOLI[4]) in normalizza(tx)]
    assert pag4[-1] in orizz, (pag4, orizz)
    return pagine, orizz, sorted(dimensioni)


def main():
    for f in (DOCX, PDF):
        if f.exists():
            f.unlink()
    genera_docx()
    assert DOCX.exists() and DOCX.stat().st_size > 0
    n_tab = gate_docx()
    celle = genera_pdf()
    assert PDF.exists() and PDF.read_bytes()[:5] == b'%PDF-'
    pagine, orizz, dim = gate_pdf()
    print(f'OK {DOCX.name}: 7 sezioni, {len(H2_ATTESI)} sottosezioni, {n_tab} tabelle, sezione 4 orizzontale')
    print(f'OK {PDF.name}: {pagine} pagine (orizzontali: {orizz}), {celle} celle senza parole spezzate, '
          f'corpi {dim[0]}–{dim[-1]} pt')
    print(f'   {DOCX.stat().st_size // 1024} KB · {PDF.stat().st_size // 1024} KB')


if __name__ == '__main__':
    main()
