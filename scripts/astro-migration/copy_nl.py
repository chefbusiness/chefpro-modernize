#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Copy neerlandés (registro formal u) para la tanda de salsas del glosario.

Doce fichas de horeca: beurre manié, napperen, monteren met boter, beurre blanc,
gastrique, liaison met eigeel, vleesglace, fumet, zetmeelpap, roux, emulsie
y demi-glace. Texto de trabajo, no un ensamblador.
"""
from __future__ import annotations

COPY = {
    "manie": {
        "title": "Beurre manié: rauwe boter en bloem aan het eind",
        "description": "Beurre manié is zachte boter en bloem in gelijke delen, rauw gewreven. U bindt er een saus mee aan het eind. Geen roux: de bloem is niet van tevoren gegaard.",
        "term": "beurre manié",
        "lead": "Beurre manié is zachte boter en bloem, koud gewreven, in gelijke delen, naar gewicht. U klopt het aan het eind door een saus die al smaak heeft. De bloem is rauw, dus dit is geen roux en hoort niet bij de basis. Op de passe redt u er een te dunne saus mee, vlak voor de gast.",
        "paras": [
            "Een beurre manié geeft een saus dikte als de smaak al af is en de lepel nog te dun loopt. U wrijft zachte boter en bloem koud tegen elkaar, in gelijke delen, naar gewicht, tot de massa egaal is. Die massa is rauw. De bloem heeft geen vuur gezien en draagt niet de smaak van een roux. Daarom hoort het gebaar aan het eind, niet bij het opzetten van een fond. Proeft u nog bloem, dan heeft de saus niet mogen doortrekken. De pan en de basis blijven dezelfde.",
            "U laat de boter zacht worden, niet gesmolten, en u wrijft de bloem erdoor tot u geen droge bloem meer ziet. Daarna klopt u kleine stukken door de pruttelende saus, weg van een harde kook, zodat het vet de bloem meteen meeneemt. Een koude homp in een saus die nauwelijks beweegt, geeft klonten. De garde blijft in uw hand tot de massa verdwenen is. Dit is een correctie, geen vervanging van de roux waarmee de saus ooit begon. U proeft voordat de pan de zaal in gaat.",
            "In de mise en place hoort beurre manié niet bij de fond. De fond, de roux en de saus hebben hun eigen moment, en deze massa blijft een ingreep voor later op de dag. Wel legt u zachte boter en bloem apart en afgedekt, zodat u niet nog moet wrijven als de borden al staan. IJskoude boter mengt niet met de bloem. Gesmolten boter wordt een vet plasje zonder greep. De brigade die dit klaarzet, verliest geen gang op het moment dat het misgaat. Een bon die binnenvalt terwijl u nog staat te wrijven, komt te laat voor deze pan.",
            "Op de passe kijkt u in de lepel. Loopt de saus eraf als water, dan is er nog tijd voor beurre manié en geen tijd voor een nieuwe roux. U klopt, u proeft, u laat de pan nog even pruttelen en dan geeft u uit. De gast krijgt een saus die aan het vlees blijft, niet een plas onder het vlees. De chef-kok proeft mee. Wacht u te lang met doortrekken, dan smaakt het naar rauwe bloem en komt het bord terug. Rauwe bloem op de tong van de gast haalt u niet meer weg van het bord.",
            "Zo raakt u de marge niet door de fond opnieuw te trekken, maar als de aandacht in de pan verslapt. Met beurre manié hoeft u geen nieuwe fond te trekken en geen roux opnieuw te garen. Een saus die schift omdat het vuur te hard staat, of die naar bloem smaakt omdat zij niet mocht doortrekken, is alsnog weg. Dan giet u product weg terwijl de zaal doorgaat. U gebruikt het gebaar als correctie met discipline, niet als excuus voor een slappe basis. De fiche zegt wanneer het mag.",
        ],
        "busca": "Zoekers schrijven beurre manié met accent of beurre manie zonder accent, en vaak alleen bloem omdat ze de rauwe kant van het gebaar bedoelen. Wie roux intikt, komt op dezelfde hoek uit en haalt de technieken door elkaar. Beurre manié hoort bij het eind van de saus, roux bij het begin. U houdt op de fiche de schrijfwijze aan die de brigade hardop gebruikt, anders legt de mise en place de verkeerde pan klaar. Napperen komt pas daarna, als u wilt zien of de saus blijft hangen.",
        "rows": [
            ("Rauw gewreven", "Boter en bloem koud samen", "Gaart de bloem niet van tevoren"),
            ("Gelijke delen", "Naar gewicht, niet naar gevoel", "Geen losse schep bloem extra"),
            ("Aan het eind", "Dikt een saus die al smaakt", "Zet geen fond of velouté op"),
            ("Na het inkloppen", "De saus trekt nog even door", "Gaat niet rauw de zaal in"),
        ],
        "faq": [
            (
                "Wat is een beurre manié?",
                "Een beurre manié is zachte boter en bloem, koud tegen elkaar gewreven, in gelijke delen, naar gewicht. U klopt die rauwe massa aan het eind door een saus die al smaak heeft. De bloem is niet gegaard, dus dit is geen roux. Op de passe vangt u er een te dunne saus mee op. De gast mag geen rauwe bloem proeven, dus de pan trekt nog even door.",
            ),
            (
                "Is beurre manié hetzelfde als een roux?",
                "Nee. Een roux gaart de bloem in vet voordat de vloeistof erbij komt. Beurre manié blijft rauw en gaat pas aan het eind door de saus. Wisselt u ze om, dan proeft de gast bloem of mist de saus de basis. Op de passe zijn het verschillende gebaren, geen synoniemen. De fiche hoort dat onderscheid hardop te maken.",
            ),
            (
                "Wanneer gebruikt u beurre manié?",
                "U grijpt ernaar als de saus al op smaak is en alleen nog te dun van de lepel loopt. Niet bij het begin van de fond, en niet in plaats van de roux die de saus draagt. Op de passe is het een correctie, geen nieuwe bereiding. Daarna laat u de pan nog doortrekken. Anders smaakt het bord naar rauwe bloem.",
            ),
            (
                "Waarom smaakt de saus naar bloem?",
                "Omdat de bloem in een beurre manié rauw de saus in gaat. Klopt u hem erdoor en geeft u meteen uit, dan heeft de bloem geen kans om te garen in de vloeistof. De gast proeft dat meteen, ook als de saus dik oogt. U laat de pan nog pruttelen en u proeft opnieuw. Een roux had dit probleem aan het begin al opgelost.",
            ),
        ],
        "alt": [
            "Zachte boter en bloem, rauw tot een egale massa gewreven op de werkbank",
            "Een garde klopt beurre manié door een pruttelende saus in een sauteerpan",
            "Een gebonden saus in de lepel, klaar om vanaf de passe uit te geven",
        ],
        "tags": '["beurre manié", "beurre manie", "saus binden", "horeca"]',
        "links": [
            ("roux", "Wat een roux anders doet dan beurre manié"),
            ("papilla", "Zetmeelpap als u zonder boter wilt binden"),
            ("napar", "Napperen: zien of de saus aan de lepel blijft"),
        ],
    },
    "napar": {
        "title": "Napperen: de saus die de lepel bedekt",
        "description": "Napperen is de test waarbij de saus de achterkant van de lepel bedekt. Het is geen saus met een eigen naam. Zo ziet u of een reductie ver genoeg is ingekookt.",
        "term": "napperen",
        "lead": "Napperen is geen saus en geen recept. Het is de test waarmee u ziet of een saus de achterkant van de lepel bedekt. Blijft er een gesloten laag op liggen, dan is de saus nappé. Op de passe beslist die test of de gast een saus krijgt die blijft hangen of een plas op het bord.",
        "paras": [
            "Napperen is een oordeel, geen bereiding met een eigen naam op de kaart. U haalt een lepel door de saus en u kijkt naar de achterkant. Blijft daar een gesloten laag op liggen, die niet meteen in banen wegloopt, dan nappeert de saus. Loopt het metaal meteen bloot, dan is zij te dun. Een saus kan nappé zijn zonder dat zij vleesglace of demi-glace heet. De test zegt iets over dikte, niet over herkomst. U herhaalt de test zodra u de saus bijstelt, anders vertrouwt u een lepel die niet meer bij deze pan hoort.",
            "U gebruikt een schone lepel, niet de garde waarmee u net heeft geklopt. De saus hoort te bewegen, niet te koken als een storm. U kantelt de lepel en u laat de laag even liggen. Trekt zij open, dan mist de saus nog binding. De chef-kok leert dit oog aan de brigade, want een foto van een lepel liegt als het licht anders valt. U proeft daarna alsnog, want nappé zegt niets over zout. Een open baan in de laag betekent dat u nog verder moet, niet dat de saus al een naam verdient.",
            "In de mise en place staat de test niet als ingrediënt. Zij hoort bij het moment waarop een reductie bijna klaar is. U plant er tijd voor, anders beslist de passe op gevoel en gaat een te dunne saus de zaal in. Een lepel bij de pan is genoeg. U schrijft op de fiche het woord napperen bij de controle, niet bij de receptregel. Zo pakt niemand een pot met de naam nappé uit de kast. Zonder dat woord bij de controle verzint iemand een pot en zoekt de brigade een saus die niet bestaat.",
            "Op de passe is de lepel het laatste woord voordat het bord vertrekt. De gast ziet het verschil zonder de term te kennen: de saus blijft op het vlees liggen of zij verzamelt zich als een plas aan de rand. Een te dikke saus die in klodders valt, is ook niet nappé. U corrigeert met vloeistof of met een binding, en u test opnieuw. Eén blik is geen excuus om de hele pan te vertrouwen. Wat de gast terugstuurt, had de lepel u kunnen zeggen voordat het bord de keuken verliet.",
            "Wie de test overslaat, raakt de marge via retouren en via saus die u daarna alsnog moet redden. Een bord dat terugkomt omdat de jus eraf liep, ontneemt de brigade een gang en de zaal een uitleg. Napperen voorkomt dat, zonder een nieuwe techniek te verzinnen. Het is een gewoonte, geen extra recept. De chef-kok die de lepel eist, beschermt de pan die al klaar was. U wint er geen nieuwe saus mee. U voorkomt dat een gaaf bord terugkomt en dat de brigade dezelfde gang opnieuw opbouwt terwijl de zaal wacht.",
        ],
        "busca": "Wie napperen zoekt, zoekt een werkwoord. Wie nappé zoekt, zoekt de toestand van de saus die de lepel bedekt. Het is dezelfde test, anders geschreven, en geen saus die op de kaart staat. Verwar het niet met demi-glace of vleesglace: die sauzen moeten nappé zijn, maar zij hebben een eigen naam. Op de fiche schrijft u napperen bij de controle, niet bij de recepten. Zo blijft de mise en place zuiver.",
        "rows": [
            ("De lepeltest", "De saus dekt de achterkant", "Geeft de saus geen eigen naam"),
            ("Nappé", "De laag blijft gesloten liggen", "Is geen recept op de kaart"),
            ("Te dun", "Het metaal loopt meteen bloot", "Wordt niet beter door te hopen"),
            ("Te dik", "De saus valt in klodders", "Is ook dan niet geslaagd"),
        ],
        "faq": [
            (
                "Wat betekent napperen?",
                "Napperen is kijken of de saus de achterkant van de lepel bedekt met een gesloten laag. Het is een test op de pan, geen saus die u apart bereidt. Blijft de laag liggen, dan is de saus nappé. Loopt zij er meteen af, dan is zij te dun. Op de passe beslist die blik of het bord de zaal in mag.",
            ),
            (
                "Is nappé een saus?",
                "Nee. Nappé beschrijft de toestand van een saus die de lepel bedekt. Vleesglace en demi-glace kunnen nappé zijn, en een velouté ook, zonder dat zij dezelfde saus worden. Zoekt u een recept onder die naam, dan zoekt u de test. Op de fiche hoort napperen bij de controle te staan, niet bij de ingrediënten.",
            ),
            (
                "Hoe ziet u of een saus nappeert?",
                "U haalt een schone lepel door de saus en u kantelt hem. Blijft op de achterkant een gesloten laag liggen, dan nappeert zij. Trekt de laag open of loopt het metaal bloot, dan is zij te dun. Valt zij in klodders, dan is zij te dik. U proeft daarna nog, want de test zegt niets over de smaak.",
            ),
            (
                "Welke sauzen moeten napperen?",
                "Elke saus die op het bord moet blijven liggen, hoort deze test te doorstaan. Demi-glace en vleesglace worden er expres naartoe gekookt. Een te dunne jus faalt, ook als de smaak klopt. De gast ziet dan een plas, geen laag. Op de passe is de lepel sneller dan een discussie over de naam van de saus.",
            ),
        ],
        "alt": [
            "Een lepel waarvan de achterkant bedekt is met een gesloten laag saus",
            "De chef-kok kantelt een lepel boven de pan om te zien of de saus nappeert",
            "Een bord waarop de saus op het vlees blijft en niet naar de rand loopt",
        ],
        "tags": '["napperen", "nappé", "saus", "horeca"]',
        "links": [
            ("glace", "Vleesglace: reduceren tot de saus nappeert en geleert"),
            ("demi", "Demi-glace, ingekookt tot hij de lepel dekt"),
            ("blanc", "Beurre blanc, die u meteen uitdeelt"),
        ],
    },
    "montar": {
        "title": "Monteren met boter: glans zonder harde kook",
        "description": "Monteren met boter is koude boter door een hete saus kloppen, weg van een harde kook. De saus krijgt glans en binding. Kookt hij hard door, dan scheidt de boter.",
        "term": "monteren met boter",
        "lead": "Monteren met boter is koude boter door een hete saus kloppen, niet op een harde kook. Het vet mengt zich en de saus krijgt glans. Gaat de pan hard aan de kook, dan scheidt de boter en ziet de gast druppels. U doet dit aan het eind, als de smaak al klopt en alleen de afwerking nog ontbreekt.",
        "paras": [
            "Monteren met boter is de afwerking waarbij koude boter in een hete saus verdwijnt onder de garde. U haalt de pan van een harde kook. De saus mag heet zijn, zij mag niet razen. Het vet mengt zich met de vloeistof en de oppervlakte wordt glanzend. Dit is geen roux en geen beurre manié: de bloem speelt hier geen rol. Het is ook niet automatisch een beurre blanc. Elke saus die u zo afwerkt, blijft haar eigen saus. De pan die u afwerkt, houdt haar eigen naam, ook als de glans daarna hetzelfde oogt.",
            "De boter komt koud uit de koeling, in stukken die de garde aankan. U klopt terwijl u de pan iets van het vuur houdt of het vuur temt. Smelt de boter alleen maar bovenop, dan heeft u niet gemonteerd, dan heeft u vet toegevoegd. De saus hoort het vet op te nemen. Blijven er ogen van vet drijven, dan was de kook te hard of de boter te snel. U stopt, u kalmeert de pan en u klopt opnieuw. Een garde die u neerlegt voordat het vet is opgenomen, laat de saus onaf gemonteerd achter.",
            "In de mise en place ligt de boter koud, niet zacht op het fornuis. Zachte boter monteert slapper en verliest het contrast met de hete saus. U snijdt haar van tevoren, zodat op de passe niemand nog een mes zoekt. De garde ligt bij de pan, niet in de lade. De chef-kok wijst aan welke sauzen dit gebaar krijgen en welke met rust gelaten worden. Niet elke pan wordt mooier van extra vet. Koude boter die al op het fornuis ligt te wachten, is op de passe geen koude boter meer en monteert slap.",
            "Op de passe monteert u vlak voor het uitgeven. De glans zakt als de saus lang blijft staan en opnieuw hard kookt. De gast ziet dan een doffe laag of spikkels vet op het bord. U geeft uit zolang de saus glanst en de boter nog opgenomen is. Komt een bord terug met een vette rand, dan was het vuur te fel of de wachttijd te lang. De chef-kok proeft en kijkt tegen het licht. In de drukte merkt u het later dan de gast, die het vet meteen op het bord ziet.",
            "Een mislukte montage raakt de marge omdat u de saus vaak niet meer rustig herstelt tijdens de service. Vet dat geschift is, haalt u er niet feilloos uit zonder de pan te belasten. U begint liever met koude boter en een kalme kook dan dat u een gescheiden saus naar de zaal stuurt. De fiche noemt het gebaar bij de afwerking. Zo grijpt de brigade niet naar bloem waar glans gevraagd wordt. Een gescheiden saus de zaal in sturen verspeelt de gang. De brigade begint die pan niet opnieuw midden in de service.",
        ],
        "busca": "In de zoekbalk hoort de volle uitdrukking monteren met boter. Alleen het woord boter levert recepten voor deeg en voor bakken, niet dit gebaar aan het eind van een saus. Beurre blanc is de saus die er helemaal op leunt. Een andere saus die u alleen afwerkt, gebruikt hetzelfde gebaar maar blijft een andere saus. U schrijft het zoals de brigade het uitspreekt, anders legt de mise en place zachte boter klaar waar u koude nodig heeft.",
        "rows": [
            ("Koude boter", "Klopt in een hete saus", "Smelt niet los bovenop"),
            ("Geen harde kook", "Het vet blijft opgenomen", "Scheidt zodra de pan raast"),
            ("Aan het eind", "Geeft glans en zachtheid", "Bouwt de saus niet op"),
            ("Meteen uitgeven", "De glans houdt kort stand", "Wacht niet op een later gang"),
        ],
        "faq": [
            (
                "Wat is monteren met boter?",
                "U klopt koude boter door een hete saus die al op smaak is, weg van een harde kook. Het vet mengt zich en de saus krijgt glans. Het is een afwerking, geen roux en geen beurre manié. Er komt geen bloem aan te pas. Op de passe doet u dit vlak voor het uitgeven, anders zakt de glans weer weg.",
            ),
            (
                "Waarom moet de boter koud zijn?",
                "Koude boter laat zich door de hete saus opnemen terwijl u klopt. Boter die al slap werd, smelt te gehoorzaam en blijft als vet bovenop drijven. U houdt de pan weg van een harde kook, anders schift het geheel alsnog. In de mise en place blijft de boter dus koud liggen. De garde doet het werk, niet het vuur alleen.",
            ),
            (
                "Wat gebeurt er op een harde kook?",
                "Dan scheidt de boter. U ziet ogen van vet en de saus verliest haar glans. De gast krijgt druppels op het bord in plaats van een samenhangende saus. U haalt de pan van de harde kook en u klopt opnieuw met een nieuw koud stuk, als de saus het nog pakt. Lukt dat niet, dan begint u die portie niet nog eens te forceren.",
            ),
            (
                "Is monteren hetzelfde als beurre blanc?",
                "Nee. Monteren met boter is het gebaar. Beurre blanc is een saus die met dat gebaar wordt opgebouwd uit sjalot, witte wijn, azijn en koude boter. U kunt een andere saus ook monteren zonder dat zij een beurre blanc wordt. Op de fiche horen de twee namen niet door elkaar te staan. De passe geeft anders het verkeerde uit.",
            ),
        ],
        "alt": [
            "Koude stukken boter naast een hete saus, klaar om gemonteerd te worden",
            "Een garde klopt boter door een saus die niet hard kookt",
            "Een glanzende saus in een pan, vlak voor zij de passe op gaat",
        ],
        "tags": '["monteren met boter", "botersaus", "saus afwerken", "horeca"]',
        "links": [
            ("blanc", "Beurre blanc: de saus die helemaal op dit gebaar leunt"),
            ("emulsion", "Waarom de ene emulsie langer houdt dan de andere"),
            ("yema", "Liaison met eigeel, een ander gebaar dan boter inkloppen"),
        ],
    },
    "blanc": {
        "title": "Beurre blanc: sjalot, wijn, azijn en koude boter",
        "description": "Beurre blanc is sjalot met witte wijn en azijn, ingekookt en gemonteerd met koude boter. Een instabiele emulsie: u serveert hem meteen en laat hem niet wachten.",
        "term": "beurre blanc",
        "lead": "Beurre blanc begint met sjalot, witte wijn en azijn die u samen reduceert. Daarna monteert u met koude boter, niet op een harde kook. Het is een instabiele emulsie zonder eigeel dat de boter vasthoudt. Daarom serveert u meteen: op de passe overleeft deze saus het wachten niet.",
        "paras": [
            "Beurre blanc is een warme botersaus. U fruit sjalot zacht, u voegt witte wijn en azijn toe en u reduceert tot de vloeistof de sjalot nog net draagt. Daarna monteert u met koude boter, weg van een harde kook. Er zit geen eigeel in dat de boter vasthoudt. Daarom is de emulsie instabiel. Dit is geen hollandaisesaus en geen vinaigrette. De smaak is botergedragen, scherp van de azijn, zacht van de sjalot. De scherpte blijft van de azijn en de zachtheid van de sjalot. U herkent hem aan die bleke glans, niet aan een kleur van eigeel.",
            "De reductie mag niet droog staan en niet als een soep blijven. U klopt de koude boter in stukken door de hete, maar kalme vloeistof. De saus wordt bleek en glanzend. Gaat zij hard koken, dan scheidt de boter en oogt het bord vettig. U houdt de pan in de hand of het vuur laag. U proeft op azijn en op zout voordat de laatste boter erin gaat. Daarna corrigeert u niet meer met een harde kook. Staat de pan toch te hard, dan haalt u haar even van het vuur en klopt u door tot de glans terug is.",
            "In de mise en place staan sjalot, witte wijn, azijn en koude boter apart. De boter blijft koud tot het moment van monteren. U reduceert liever per keer dan een grote pan die moet wachten. De chef-kok zet de beurre blanc dicht bij de passe, niet achteraan op een heet fornuis. Een garde en een schone lepel liggen erbij. Wie de reductie van tevoren te ver doorzet, heeft straks niets om de boter in te dragen. Een reductie die u te ver heeft doorgezet, heeft straks geen vocht meer om de boter te dragen.",
            "Op de passe serveert u meteen. De gast krijgt de saus glanzend, niet gescheiden. Laat u de pan staan, dan zakt de emulsie en komt het vet bovendrijven. Opwarmen op een harde kook maakt het erger. Een bord dat wacht onder de lamp, verliest wat u net heeft opgebouwd. De chef-kok geeft deze saus uit in het tempo van de tafel, niet in het tempo van een voorraadpan. Wie hem naast de lamp parkeert, serveert de gast vet in plaats van saus. U monteert pas als het bord al in de hand is.",
            "De marge lijdt als u een beurre blanc te vroeg maakt en daarna weggooit. De boter is dan al opgenomen en de reductie is op. U plant de saus bij de uitgifte, niet al in de mise en place. Een gescheiden pan redt u zelden tot dezelfde glans. Liever een kleine hoeveelheid op het juiste moment dan een volle pan die de service niet overleeft. De fiche zegt: monteren en meteen de zaal in. Wie te vroeg monteert, speelt met de marge en gooit boter weg die de service nog nodig had.",
        ],
        "busca": "Wie beurre blanc zoekt, schrijft de Franse naam, in twee woorden, niet aan elkaar geplakt en niet vertaald tot alleen witte boter. Wie alleen boter zoekt, mist de sjalot, de witte wijn en de azijn. Het gebaar erachter is monteren met boter, en dat zoekt u apart als u de techniek wilt zonder het hele recept. Op de kaart mag de Franse naam blijven. Op de fiche zet u erbij dat de saus meteen de passe op gaat.",
        "rows": [
            ("Sjalot, wijn, azijn", "Eerst reduceren", "Geen olie en geen eigeel"),
            ("Koude boter", "Monteren tot een bleke saus", "Niet op een harde kook"),
            ("Instabiel", "Houdt alleen als u meteen serveert", "Geen voorraad voor de hele service"),
            ("Geen hollandaisesaus", "De scherpte komt van azijn", "Wordt niet stijf van eigeel"),
        ],
        "faq": [
            (
                "Wat is een beurre blanc?",
                "Een beurre blanc is sjalot met witte wijn en azijn, gereduceerd, en daarna gemonteerd met koude boter. U houdt de pan weg van een harde kook. Het wordt een bleke, glanzende saus. Er zit geen eigeel in. Daarom is het geen hollandaisesaus. U serveert hem meteen, want de emulsie laat los als hij blijft staan.",
            ),
            (
                "Waarom is een beurre blanc instabiel?",
                "Omdat niets stevigs de boter vasthoudt. Er is geen eigeel en geen lecithine die de emulsie draagt, alleen de manier van kloppen en de warmte van de reductie. Zodra de saus te hard kookt of te lang wacht, scheidt het vet. De gast ziet dan druppels. Op de passe maakt u hem daarom op het moment van uitgeven.",
            ),
            (
                "Kunt u een beurre blanc laten wachten?",
                "Niet zoals een saus met eigeel. Zet u de pan weg, dan zakt de emulsie. Een harde kook om hem weer warm te krijgen, scheidt de boter verder. U houdt hem hooguit kort warm, weg van de kook, en u geeft uit. In de mise en place staat de reductie klaar, de boter koud. Monteren doet u als de gast aan tafel zit.",
            ),
            (
                "Zit er eigeel in een beurre blanc?",
                "Nee. De saus is sjalot, witte wijn, azijn en koude boter. Eigeel zou hem naar een andere familie trekken, dichter bij een hollandaisesaus. Dat is een ander recept en een andere houdbaarheid. Op de fiche staat geen ei bij beurre blanc. De passe hoeft er ook niet naar te zoeken in de mise en place.",
            ),
        ],
        "alt": [
            "Sjalot die met witte wijn en azijn staat te reduceren in een pan",
            "Koude boter die met een garde door een bleke reductie wordt geklopt",
            "Een glanzende beurre blanc die meteen vanaf de passe wordt uitgegeven",
        ],
        "tags": '["beurre blanc", "botersaus", "emulsie", "horeca"]',
        "links": [
            ("montar", "Monteren met boter, het gebaar achter deze saus"),
            ("emulsion", "Waarom deze emulsie minder stabiel is"),
            ("gastrique", "Gastrique: zoet en zuur, zonder gemonteerde boter"),
        ],
    },
    "gastrique": {
        "title": "Gastrique: suikerkaramel losgemaakt met azijn",
        "description": "Een gastrique is suikerkaramel losgemaakt met azijn. Zoet en zuur in één basis voor de saus, geen vinaigrette en geen emulsie van olie. U bouwt de saus eromheen.",
        "term": "gastrique",
        "lead": "Een gastrique is suikerkaramel die u losmaakt met azijn. Zoet en zuur zitten in één basis, en daar bouwt u de saus omheen. Het is geen vinaigrette: er komt geen olie aan te pas en er ontstaat geen emulsie. De gast proeft die lijn in de saus, niet een dressing ernaast.",
        "paras": [
            "Een gastrique begint als suiker die u tot karamel laat gaan en daarna losmaakt met azijn. Het zoet en het zuur komen in dezelfde basis samen. U bouwt daar een saus omheen, vaak bij fruit, bij een braadstuk of bij een panvocht dat meer ruggengraat nodig heeft. Er komt geen olie aan te pas. Daarom is dit geen vinaigrette en geen emulsie. De lijn is strak: karamel en azijn, niet een slasaus die u er los bij schept. U schept hem door de saus, u zet hem niet als een aparte lepel zoet naast het vlees.",
            "U smelt de suiker droog of met heel weinig vocht tot zij karamel wordt. Te bleek blijft zij naar suiker smaken, te ver wordt zij bitter en donker. Dan maakt u de karamel los met azijn. De pan sist. U roert tot de karamel weer vloeit en er geen harde stukken meer op de bodem zitten. Proef. Te scherp verlengt u met het vocht van de saus later, niet met een slok olie. Te zoet vraagt om meer van dezelfde azijnlijn, met beleid. Harde stukken op de bodem betekenen dat de karamel nog niet echt is losgemaakt.",
            "In de mise en place staan suiker en azijn bij de saussectie, niet bij de salades. De brigade die een vinaigrette draait, pakt anders de verkeerde fles en denkt dat het hetzelfde is. U labelt de pot gastrique zodra zij afgekoeld en vloeibaar is. Een harde klomp karamel is geen voorraad. De chef-kok laat zien hoe ver de kleur mag gaan, want dat oog leert u niet uit een naam alleen. De passe verwacht een basis, geen experiment. Een pot zonder naam verdwijnt tussen de vinaigrettes en komt op het verkeerde bord terecht.",
            "Op de passe gebruikt u de gastrique als ruggengraat van de saus, niet als een lepel zoet bovenop het bord. De gast proeft karamel en azijn in één lijn, gedragen door het vocht van het gerecht. Een bittere, verbrande toon overheerst het vlees en komt terug. Een te zure toon doet hetzelfde. U proeft in de pan, niet op het bord van de gast. De saus hoort af te zijn voordat zij de passe verlaat. U bouwt de lijn in de pan af, zodat de passe alleen nog hoeft uit te geven.",
            "Verbrande karamel giet u weg. Dat raakt de marge, want suiker en tijd zijn dan op en de pan moet schoon voor de volgende ronde. Een vinaigrette die u per ongeluk als gastrique inzet, haalt u niet meer uit een warme saus. De fiche noemt azijn en suiker, niet olie. Zo blijft de hoek van de keuken zuiver. De chef-kok bewaakt dat onderscheid, vooral als de service snel gaat. Een verbrande pan begint u leeg opnieuw. Suiker die bitter is, haalt u met geen azijn meer recht.",
        ],
        "busca": "Gastrique blijft in het Frans op de fiche, omdat een vertaling naar zoetzure saus hem verwart met een vinaigrette. U zoekt het woord gastrique als u suikerkaramel bedoelt die met azijn is losgemaakt. Zoet en zuur, zonder olie. Wie vinaigrette intikt, komt bij een emulsie van azijn en olie uit, en dat is een ander gebaar. U zet de twee namen niet op één regel alsof zij synoniem zijn. De brigade pakt anders de verkeerde fles.",
        "rows": [
            ("Suikerkaramel", "Zoet dat kleur en geur draagt", "Blijft niet bleek als siroop"),
            ("Losmaken met azijn", "Het zuur haalt de karamel los", "Geen olie erdoor kloppen"),
            ("Geen vinaigrette", "Een basis voor warme saus", "Geen dressing voor de sla"),
            ("Te ver gekaramelliseerd", "Wordt bitter", "Redt u niet met extra suiker"),
        ],
        "faq": [
            (
                "Wat is een gastrique?",
                "Een gastrique is suikerkaramel die u losmaakt met azijn. Zoet en zuur zitten in één basis, en daaromheen bouwt u de saus. Er komt geen olie aan te pas. Het is dus geen vinaigrette en geen emulsie. Op de passe geeft hij lijn aan een jus of een saus bij fruit of vlees. De gast proeft die lijn in de saus zelf.",
            ),
            (
                "Is een gastrique een vinaigrette?",
                "Nee. Een vinaigrette is een emulsie van azijn en olie, koud of lauwwarm, voor sla en bijgerechten. Een gastrique kent geen olie. Het is karamel losgemaakt met azijn, een basis voor een warme saus. Zet u ze op dezelfde fiche-regel, dan pakt de brigade de verkeerde fles. De passe merkt dat aan een saus die vettig wordt in plaats van strak.",
            ),
            (
                "Waarmee maakt u de karamel los?",
                "Met azijn. De suiker gaat eerst tot karamel, daarna giet u de azijn erbij en u roert tot alles weer vloeit. Water alleen geeft geen gastrique, olie evenmin. Te bleke suiker smaakt zoet zonder diepte, te donkere karamel wordt bitter. U proeft voordat de basis de saus in gaat. Op de fiche staat azijn, niet een andere fles uit de mise en place.",
            ),
            (
                "Wanneer zet u een gastrique in?",
                "Als een saus zoet en zuur in één lijn nodig heeft, bijvoorbeeld bij fruit of bij een braadvocht dat anders alleen naar fond smaakt. U mengt de gastrique door de saus, u serveert hem niet als een lepel siroop op het bord. De gast hoort hem in de saus te proeven. Een verbrande pan begint u opnieuw, die redt u niet op de passe.",
            ),
        ],
        "alt": [
            "Suiker die in een pan tot een amberkleurige karamel verkleurt",
            "Azijn die een karamel losmaakt terwijl de pan sist",
            "Een saus met een zoetzure lijn, klaar op de passe naast het vlees",
        ],
        "tags": '["gastrique", "karamel", "azijn", "horeca"]',
        "links": [
            ("blanc", "Beurre blanc, waarin azijn een andere rol speelt"),
            ("demi", "Demi-glace, de bruine saus waar een gastrique soms lijn aan geeft"),
            ("yema", "Liaison met eigeel, als de saus dikte nodig heeft in plaats van zoet"),
        ],
    },
    "yema": {
        "title": "Liaison met eigeel: binden zonder te schiften",
        "description": "Een liaison met eigeel bindt saus of soep. U tempert het eigeel met een beetje hete vloeistof en giet het terug in de pan. Kookt het, dan schift het ei.",
        "term": "liaison met eigeel",
        "lead": "Een liaison met eigeel bindt een saus of een soep zonder er een hollandaisesaus van te maken. U tempert het eigeel met een beetje hete vloeistof en giet het terug in de pan. Kookt het daarna door, dan schift het ei. De gast ziet stukjes in plaats van een gladde binding, en de pan is verloren.",
        "paras": [
            "Een liaison met eigeel is een binding. U gebruikt het eigeel om een saus of een soep dikker en ronder te maken, niet om een botersaus op te bouwen. Het is geen hollandaisesaus. Daar klopt u boter in eigeel tot een emulsie. Hier gaat het eigeel de pan in die al vloeistof is. Het verschil zit in het gebaar en in het gevaar: kookt de liaison, dan schift het ei. De saus hoort glad te blijven. De binding hoort de saus ronder te maken, niet hem in een botersaus te veranderen.",
            "U tempert eerst. Een beetje hete vloeistof gaat al roerend door het eigeel, tot dat mengsel warm aanvoelt en niet meer schrikt. Dan giet u het terug in de pan. Het vuur staat laag. U roert. Zodra de saus aan de kook komt, stolt het ei in vlokken. Dan is de pan verloren voor deze binding. U haalt de pan op tijd van het harde vuur. De lepel toont of de binding pakt, de tong of zij schoon is. Een pan die u even alleen laat, is genoeg om die binding te verliezen.",
            "In de mise en place staat het eigeel apart van het eiwit. Het wit hoort niet in deze binding, dat wordt draderig en schift eerder lelijk. U zet alleen klaar wat de pan deze service nodig heeft, en de rest van het eigeel blijft koud. De chef-kok laat de brigade het tempereren zien, niet alleen de naam liaison. Een kom, een garde en een lepel hete saus zijn de hele opstelling. Het eiwit blijft apart, want dat wordt draderig en hoort niet in deze kom. De brigade ziet dat verschil voordat de pan heet is.",
            "Op de passe is een geschifte liaison een stille ramp. De gast ziet vlokjes en proeft ei in plaats van saus. U kunt die pan niet door een zeef redden tot de oorspronkelijke glans. U geeft niet uit wat geschift is. De chef-kok stopt de gang liever een moment dan een bord met stukjes de zaal in te sturen. Een liaison die net pakt, gaat meteen weg van de kook en meteen het bord op. Vlokjes op het bord verraden de fout aan de gast, ook als de rest van de smaak nog meevalt.",
            "De marge zit in de pan die u weg moet gieten. Eigeel is dan op, de saus eromheen ook, en de service wacht. Temperen voelt langzamer en is sneller dan opnieuw beginnen. De fiche zegt: temperen, terug in de pan, niet laten koken. Wie dat overslaat om tijd te winnen, verliest de gang. De chef-kok bewaakt het vuur persoonlijk bij deze binding, zeker als de passe vol staat. De brigade die het vuur deelt met een andere pan, merkt het in de marge pas als de gang al stilstaat.",
        ],
        "busca": "Zoekt u liaison en eigeel samen, dan zoekt u het binden van een saus of een soep. Liaison alleen is te breed, eigeel alleen levert recepten voor bakken. Op deze fiche tempert u het eigeel en giet u het terug. Hollandaisesaus is een andere zoekterm: dat is een emulsie van boter, geen binding die in de pan mag koken. U zet eigeel op de fiche, niet het hele ei, anders staat het wit mee in de mise en place.",
        "rows": [
            ("Eigeel temperen", "Eerst een beetje hete vloeistof", "Niet rauw in de kokende pan"),
            ("Terug in de pan", "De binding pakt zacht", "De saus mag niet doorkoken"),
            ("Kookt het", "Het ei schift in vlokken", "Een zeef haalt de glans niet terug"),
            ("Geen hollandaisesaus", "U bindt een bestaande vloeistof", "U bouwt geen boteremulsie"),
        ],
        "faq": [
            (
                "Wat is een liaison met eigeel?",
                "Het is een binding van een saus of een soep met eigeel. U maakt er geen hollandaisesaus van en u klopt er geen boter in tot een emulsie. Het eigeel gaat, na tempereren, terug in de pan die al vloeistof is. Kookt die pan, dan schift het ei. Op de passe geeft u alleen uit wat glad blijft. De gast mag geen vlokjes zien.",
            ),
            (
                "Hoe tempert u het eigeel?",
                "U roert een beetje hete vloeistof uit de pan door het eigeel, tot het mengsel niet meer koud schrikt. Daarna giet u het terug en u houdt het vuur laag. Slaat u die stap over, dan stolt het ei zodra het de hete saus raakt. In de mise en place staat het eigeel apart van het wit. Het wit hoort niet in deze binding.",
            ),
            (
                "Waarom schift een liaison?",
                "Omdat het ei kookt. Het stolt dan in vlokken en de saus verliest haar gladde binding. Te heet vuur, of een pan die u even alleen laat, is genoeg. De gast ziet stukjes en proeft ei. U haalt de pan van de kook zodra de binding pakt. Een geschifte pan begint u niet opnieuw met dezelfde lepel hoop.",
            ),
            (
                "Is een liaison een hollandaisesaus?",
                "Nee. Een hollandaisesaus is een emulsie: boter geklopt in eigeel. Een liaison bindt een saus of soep die al bestaat. Het vuur mag bij de liaison net niet koken, en bij de hollandaisesaus bouwt u een andere structuur. Op de fiche zijn dat andere woorden. De passe pakt anders boter waar alleen eigeel bedoeld was.",
            ),
        ],
        "alt": [
            "Eigeel in een kom, terwijl een beetje hete saus erdoor wordt geroerd",
            "De getemperde liaison gaat terug in een pan die niet hard kookt",
            "Een gladde gebonden saus zonder vlokjes ei, klaar voor de passe",
        ],
        "tags": '["liaison", "eigeel", "saus binden", "horeca"]',
        "links": [
            ("emulsion", "Emulsie: wat een hollandaisesaus wel is"),
            ("montar", "Monteren met boter, zonder eigeel"),
            ("papilla", "Zetmeelpap als u het ei wilt vermijden"),
        ],
    },
    "glace": {
        "title": "Vleesglace: glace de viande die koud geleert",
        "description": "Vleesglace, of glace de viande, is bruine fond verder gereduceerd tot hij nappeert en koud geleert. Hij gaat verder dan demi-glace. U werkt er sauzen mee af.",
        "term": "vleesglace",
        "lead": "Vleesglace, de glace de viande, is bruine fond die u verder reduceert tot hij nappeert en koud geleert. Dat gaat verder dan een demi-glace, die alleen hoeft te napperen. U werkt er een saus mee af, u zet er geen kom van voor de gast. Op de passe blijft het een concentraat, geen gang op zich.",
        "paras": [
            "Vleesglace is bruine fond die u inkookt tot hij de lepel bedekt en, als hij koud wordt, geleert. Dat is verder dan demi-glace. Een demi-glace nappeert en blijft een saus. De vleesglace gaat door tot hij bijna een gelei is, donker en geconcentreerd. U serveert hem niet als bordsoep en niet als een kom op zich. U werkt er een jus of een saus mee af, of u geeft een braadvocht de laatste diepte. De naam glace de viande is dezelfde reductie. U herkent hem aan de gelei, niet aan een saus die alleen maar donker is.",
            "U reduceert zacht. Een harde kook stoort het oppervlak en jaagt de pan naar aanbranden op de rand. U schept het vel af dat niet bij de glace hoort. De lepel is uw maat: hij moet napperen. Daarna koelt u een lepeltje op een bord. Geleert dat, dan is de reductie ver genoeg. Blijft het vloeibaar als een gewone saus, dan is het nog demi-glace of gewoon ingekookte fond. U proeft. Verder inkoken maakt hem ook zouter. Een lepeltje dat koud vloeibaar blijft, is nog geen glace, hoe donker de pan ook oogt.",
            "In de mise en place is vleesglace een pot, geen pan die u tijdens de service nog verder reduceert. U maakt hem als de brigade ruimte heeft, u koelt hem, en u bewaart hem afgedekt. Het etiket zegt vleesglace of glace de viande, niet demi-glace. De chef-kok wil dat verschil op de pot zien, want de passe grijpt anders de verkeerde diepte. Een lepel glace in een saus is een ander gebaar dan een pollepel demi-glace. De pot die demi-glace heet terwijl hij al geleert, stuurt de passe de verkeerde diepte in.",
            "Op de passe gebruikt u weinig en met opzet. De gast proeft concentratie, niet een zout waas dat de rest van het bord uitwist. Een te ver doorgekookte glace overheerst. Een te korte reductie geeft de saus geen ruggengraat. U lost een beetje glace op in het braadvocht en u laat hem niet opnieuw hard koken tot hij schift of bitter wordt. De chef-kok proeft de laatste lepel. Daarna gaat het bord weg. U lost weinig op in het braadvocht, zodat de gast het vlees nog proeft en niet alleen zout.",
            "De marge zit in de fond zelf. Dagen trekken en dan aanbranden op de bodem is een pan weg, niet een ongelukje van één service. U reduceert met aandacht, u labelt eerlijk, en u verwart de pot niet met demi-glace. Een kom soep van vleesglace de zaal in sturen, verspilt het concentraat en stelt de gast teleur. De fiche zegt: afwerken, niet opdienen als gang. Zo blijft de pot meegaan. Fond die u lang heeft getrokken en dan laat aanbranden, voelt u in de marge harder dan een mislukt bord.",
        ],
        "busca": "Vleesglace en glace de viande zijn dezelfde reductie. De Nederlandse naam zoekt de kok die in het Nederlands denkt, de Franse naam staat op de klassieke fiche. Beide moeten uitkomen bij een fond die nappeert en koud geleert, verder dan demi-glace. Schrijft u alleen glace, dan mengt u het met demi-glace en met glace van andere grondstoffen. U zet vleesglace voluit op de pot in de mise en place, anders pakt de passe de verkeerde reductie.",
        "rows": [
            ("Bruine fond", "Verder inkoken dan demi-glace", "Blijft geen gewone saus"),
            ("Nappeert", "De lepel blijft bedekt", "Is dan nog niet automatisch gelei"),
            ("Koud geleert", "Zo herkent u de glace", "Serveert u niet als bordsoep"),
            ("Afwerken", "Diepte in jus en saus", "Geen kom voor de gast"),
        ],
        "faq": [
            (
                "Wat is vleesglace?",
                "Vleesglace, of glace de viande, is bruine fond die u reduceert tot hij nappeert en koud geleert. Hij is geconcentreerder dan demi-glace. U werkt er sauzen en jus mee af. U zet er geen kom van voor de gast. Op de passe is het een concentraat, geen soep. Het etiket op de pot hoort die naam te dragen, niet die van een lichtere saus.",
            ),
            (
                "Is glace de viande hetzelfde als demi-glace?",
                "Nee. Glace de viande en vleesglace zijn dezelfde, verder doorgevoerde reductie. Demi-glace is Spaanse saus plus bruine fond, ingekookt tot hij nappeert, en hij geleert niet als een glace. Verwart u de potten, dan wordt de saus of te zwaar of te dun. Op de fiche en op het etiket blijven de namen uit elkaar. De passe proeft het verschil meteen.",
            ),
            (
                "Wanneer is de vleesglace klaar?",
                "Als hij de achterkant van de lepel bedekt en een afgekoeld lepeltje geleert. Nappeert hij wel maar blijft hij koud vloeibaar als een saus, dan is hij nog niet ver genoeg. Een harde kook versnelt alleen het aanbranden. U proeft ook: verder inkoken maakt hem zouter en smaller. De chef-kok beslist op lepel en op smaak, niet op de klok.",
            ),
            (
                "Serveert u vleesglace als soep?",
                "Nee. Het is geen bordsoep en geen gang op zich. De gast zou een te zoute, te zware kom krijgen en u zou het concentraat verspillen. U lost een weinig op in een saus of een braadvocht. In de mise en place staat de pot bij de afwerking. Op de passe blijft hij daar. Een kom soep komt uit een andere pan.",
            ),
        ],
        "alt": [
            "Bruine fond die in een pan verder inkookt tot een donkere, trage glace",
            "Een afgekoelde lepel vleesglace die geleert in plaats van weg te lopen",
            "Een jus op het bord, afgewerkt met vleesglace, klaar op de passe",
        ],
        "tags": '["vleesglace", "glace de viande", "fond", "horeca"]',
        "links": [
            ("demi", "Demi-glace stopt eerder: hij nappeert, hij geleert niet zo"),
            ("fumet", "Fumet: de visfond, niet gebrand als deze bruine fond"),
            ("napar", "Napperen, de test die ook voor vleesglace geldt"),
        ],
    },
    "fumet": {
        "title": "Fumet: visfond van graten, niet gebrand",
        "description": "Fumet, ook visfond of visfumet, trekt uit visgraten en aromaten. De graten brandt u niet, anders dan bij een bruine fond. Te lang gekookt wordt hij bitter.",
        "term": "fumet",
        "lead": "Fumet is een visfond, ook visfumet genoemd, getrokken van visgraten en aromaten. U brandt de graten niet, zoals u dat bij een bruine fond wel doet. Blijft de pan te lang op het vuur, dan wordt hij bitter. Het is een basis voor de saus, geen bordsoep die u de gast voorzet.",
        "paras": [
            "Een fumet is de lichte fond van vis. U laat visgraten en aromaten trekken in water, zonder de graten eerst te branden zoals bij een bruine fond. Visfond en visfumet zijn dezelfde familie. De fond blijft bleek en ruikt naar vis die schoon is, niet naar aangebrande graat. U zeeft hem zonder hem door een doek te persen tot de troebelheid meekomt. Dit is de basis onder een saus, niet het bord dat de zaal in gaat. Persen door de doek haalt troebelheid mee die u daarna niet meer uit de saus krijgt.",
            "Te lang op het vuur wordt de fumet bitter. De graten geven dan een harde, droge toon af die u niet meer wegproeft. U houdt de trekking kalm. Een razende kook maakt hem troebel en jaagt die bittere noot naar voren. U schept schuim af. U stopt als de geur nog fris is. Een bruine fond mag verder en donkerder, deze pan niet. De lepel en de neus beslissen, niet de gewoonte van de vleeshoek. Schuim dat u laat meekoken, maakt de fond troebel en haalt een wrange toon naar voren.",
            "In de mise en place liggen de graten schoon, zonder kieuwen en zonder bloed dat de fond troebel en wrang maakt. Aromaten staan apart, fijn genoeg om geur te geven en niet zo fijn dat u pulp kookt. De chef-kok wil een andere pan dan die van de bruine fond, zodat aangebrande suikers niet meeliften. Het etiket zegt fumet, visfond of visfumet, één keuze per huis, dezelfde pot. De passe hoeft niet te gokken. Kieuwen en bloed maken de fond wrang, ook als de graten verder schoon leken op de plank.",
            "Op de passe komt de fumet niet als bordsoep naar buiten. De gast krijgt een saus of een gerecht dat op deze fond steunt, niet een kom graatwater. Bittere fumet proeft u in de saus meteen, hoe netjes het bord ook staat. U bouwt de saus eerder en u warmt haar zacht op. Een harde kook op het laatst haalt de bittere toon terug. De chef-kok proeft de basis voordat zij de saus in gaat. Bittere fond in de saus proeft de gast ook als het bord verder netjes staat.",
            "Giet u een bittere pan weg, dan raakt dat de marge: graten, tijd en de saus die u erop had willen bouwen zijn kwijt. Een te lange trekking is de gewone oorzaak, niet een geheim ingrediënt. U stopt op geur. U brandt de graten niet om hem op vlees te laten lijken. De fiche zegt visfond, niet bruine fond. Zo blijft de vissectie haar eigen pan houden. Een aangebrande rand uit de vleespan lift mee in de lepel en maakt de visjus hard, ook als de geur eerst nog fris leek.",
        ],
        "busca": "Fumet, visfond en visfumet wijzen in de Nederlandse keuken naar dezelfde basis van visgraten. Fumet is het Franse woord dat de brigade vaak hardop zegt, visfond de naam op de Nederlandse fiche, visfumet de samenstelling die zoekers intikken. U brandt deze fond niet. Verwar hem niet met een bordsoep en niet met een bruine fond van kalf. Wie alleen vis intikt, vindt recepten voor de gast, niet de pan die achter de saus staat.",
        "rows": [
            ("Visgraten en aromaten", "Een bleke fond", "De graten worden niet gebrand"),
            ("Korte, kalme trekking", "De geur blijft fris", "Te lang wordt hij bitter"),
            ("Geen bordsoep", "Basis onder de saus", "Geen kom de zaal in"),
            ("Niet de bruine fond", "Andere pan, ander vuur", "Geen kalfsgeur forceren"),
        ],
        "faq": [
            (
                "Wat is een fumet?",
                "Een fumet is een visfond van visgraten en aromaten. U brandt de graten niet, anders dan bij een bruine fond. De trekking blijft kalm. Te lang op het vuur wordt hij bitter. U serveert hem niet als bordsoep. Het is de basis onder een saus. Op de pot mogen ook de namen visfond en visfumet staan, als het huis één woord kiest en dat volhoudt.",
            ),
            (
                "Is visfond hetzelfde als visfumet?",
                "In de keuken wel. Visfond is de Nederlandse naam, visfumet de vorm die zoekers vaak intikken, fumet het woord dat de brigade hardop zegt. Alle drie horen bij graten die niet gebrand zijn. U zet één naam op het etiket zodat de passe niet twijfelt. Een bruine fond hoort niet in die pot. De fiche houdt die scheiding zichtbaar.",
            ),
            (
                "Waarom wordt een fumet bitter?",
                "Omdat hij te lang trekt of te hard kookt. De graten geven dan een droge, bittere toon af die in de saus blijft hangen. De gast proeft dat ook als het bord mooi is. U houdt de pan kalm en u stopt als de geur nog fris is. Aanbranden of meeliften met de vleesfond maakt het erger. Een bittere pan giet u weg.",
            ),
            (
                "Is een fumet een bordsoep?",
                "Nee. Het is geen gang die u de gast voorzet. Een kom van de fond smaakt naar graat en verspilt de basis die de saus nodig heeft. Op de passe bouwt u er een saus of een gerecht mee, u schept hem niet als soep. In de mise en place staat de pot bij de fond, niet bij de soeppan van de dag. ",
            ),
        ],
        "alt": [
            "Schone visgraten en aromaten in een pan, niet gebrand, klaar om te trekken",
            "Een bleke visfond die door een zeef gaat zonder troebel persvocht",
            "Een lichte vissaus op basis van fumet, afgemaakt voor de passe",
        ],
        "tags": '["fumet", "visfond", "visfumet", "horeca"]',
        "links": [
            ("glace", "Vleesglace: de bruine fond wel gebrand en ver gereduceerd"),
            ("napar", "Ook een visjus hoort te napperen voor hij uitgaat"),
            ("papilla", "Zetmeelpap als de visjus binding nodig heeft"),
        ],
    },
    "papilla": {
        "title": "Zetmeelpap: koud losgeroerd, dan in de saus",
        "description": "Zetmeelpap is zetmeel losgeroerd in koude vloeistof en daarna in de pruttelende saus. Hij bindt snel. Anders dan een roux dooft hij de glans. Bloem hoort er niet in.",
        "term": "zetmeelpap",
        "lead": "Zetmeelpap is zetmeel dat u eerst losroert in koude vloeistof en daarna in de pruttelende saus giet. Hij bindt snel en gelijkmatig, zolang u hem niet droog in de pan strooit. Anders dan een roux dooft hij de glans. De gast ziet een dikke saus die matter oogt dan een roux.",
        "paras": [
            "Een zetmeelpap is zetmeel dat u losroert in koude vloeistof tot er geen korrel meer droog ligt. Dat papje gaat daarna in de pruttelende saus. Het zetmeel bindt en de saus wordt dikker. Bloem is hier niet het middel. Bloem hoort in een roux, waar zij eerst in vet gaart, of in een beurre manié. Puur zetmeel werkt anders. Het pakt snel. En het dooft de glans. Een saus die glom, oogt na deze binding matter. Die mattere glans is een eigenschap, geen ongeluk dat u met harder roeren terugkrijgt.",
            "Strooit u het zetmeel droog in de hete pan, dan ontstaan klonten die de garde niet meer vangt. De koude vloeistof verdeelt de korrel eerst. U giet de pap al roerend in de saus die beweegt, niet in een pan die stilstaat. U laat haar nog even doortrekken zodat de binding schoon wordt en niet naar rauw zetmeel smaakt. Een harde kook is niet nodig en jaagt de saus tegen de rand. De lepel toont de dikte, het oog de doffe glans. Rauw zetmeel op de tong betekent dat de saus nog niet heeft mogen doortrekken.",
            "In de mise en place staat het zetmeel droog en afgedekt, en de koude vloeistof apart. U maakt de pap op het moment dat de saus haar nodig heeft, niet ruim van tevoren, tot zij uitzakt. De chef-kok legt vast welke sauzen glans moeten houden en dus geen zetmeelpap krijgen. Een roux of monteren met boter blijft daar de afwerking. De fiche noemt het woord zetmeelpap, niet bloem, anders pakt de brigade het verkeerde blik. Het blik met zetmeel staat niet naast de bloem, anders grijpt een hand mis in de drukte.",
            "Op de passe is de doffe saus een keuze die u bewust maakt, niet een verrassing. De gast ziet een mat oppervlak en proeft, als u te ver gaat, een lijmige binding. Dat komt terug als het gerecht glans beloofde. U bindt tot de lepel klopt en u stopt. Extra pap maakt de saus niet verfijnder, alleen zwaarder. De chef-kok kijkt tegen het licht. Een doffe jus bij een gerecht dat hoort te glanzen, stuurt u niet de zaal in. Een matte jus verrast de gast als het gerecht glans had beloofd op de kaart.",
            "Aan klonten lijdt de marge en aan sauzen die u te ver heeft gebonden en daarna moet verdunnen of weggooien. Zetmeel vraagt weinig aandacht als u het koud losroert, en de hele pan als het misgaat. U gebruikt het waar glans niet het punt is, of waar u geen roux meer kunt opzetten. De fiche zegt wanneer wel en wanneer niet. Zo grijpt de passe niet uit gewoonte naar het blik. Verdunnen achteraf haalt de smaak uit elkaar en de saus komt niet meer terug op het punt waar zij was.",
        ],
        "busca": "Zetmeelpap is het woord op deze fiche. Bloem is iets anders: bloem hoort in een roux of in een beurre manié, niet losgeroerd als zetmeel. Wie alleen pap zoekt, vindt ook desserts, dus u zet er zetmeel voor. De saus die u ermee bindt, verliest glans, en dat is geen fout in het licht maar een eigenschap van het zetmeel. U schrijft zetmeelpap op de fiche zodat de mise en place geen bloem pakt.",
        "rows": [
            ("Koud losroeren", "Het zetmeel verdeelt zich", "Niet droog in de hete pan"),
            ("In de pruttelende saus", "De binding pakt snel", "Een stilstaande pan geeft klonten"),
            ("Dooft de glans", "De saus wordt matter", "Houdt niet de glans van een roux"),
            ("Geen bloem", "Puur zetmeel, geen roux", "Vervangt geen beurre manié"),
        ],
        "faq": [
            (
                "Wat is een zetmeelpap?",
                "U roert zetmeel los in koude vloeistof tot er geen droge korrel meer is, en u giet dat in de pruttelende saus. De saus bindt snel. Het is geen roux: de bloem daarin gaart eerst in vet. Het is ook geen beurre manié. Het zetmeel dooft de glans. Op de passe kiest u dit gebaar alleen als een matte binding past bij het bord.",
            ),
            (
                "Waarom eerst in koude vloeistof?",
                "Omdat droog zetmeel in een hete saus meteen klontert. De koude vloeistof verdeelt de korrel voordat de hitte hem laat binden. Daarna giet u de pap in een saus die beweegt, terwijl u roert. In de mise en place blijven zetmeel en koude vloeistof apart tot dat moment. Een pap die u veel te vroeg maakt, zakt uit en verdeelt niet meer schoon.",
            ),
            (
                "Wat doet zetmeelpap met de glans?",
                "Hij dooft de glans. Een saus die glom van een roux of van gemonteerde boter, oogt daarna matter. Dat is een eigenschap van het zetmeel, geen fout van het licht op de passe. De gast ziet het. U gebruikt de pap waar die doffe binding geen probleem is. Waar glans bij het gerecht hoort, kiest u een ander gebaar.",
            ),
            (
                "Is zetmeelpap een roux?",
                "Nee. Een roux is bloem die u eerst in vet gaart, vóór de vloeistof erbij komt. Zetmeelpap is zetmeel, koud losgeroerd, zonder dat garen in vet. Bloem hoort er niet in. Op de fiche horen ze niet bij elkaar. De mise en place pakt anders het verkeerde blik en de saus verliest de glans die u wilde houden.",
            ),
        ],
        "alt": [
            "Zetmeel dat in koude vloeistof wordt losgeroerd tot een gladde pap",
            "De pap gaat al roerend in een pruttelende saus, zonder droge klonten",
            "Een gebonden saus met een mattere glans dan een roux, klaar voor de passe",
        ],
        "tags": '["zetmeelpap", "zetmeel", "saus binden", "horeca"]',
        "links": [
            ("roux", "Roux: bloem eerst gegaard in vet"),
            ("manie", "Beurre manié, de rauwe boter met bloem aan het eind"),
            ("yema", "Liaison met eigeel als u geen zetmeel wilt"),
        ],
    },
    "roux": {
        "title": "Wat is een roux: bloem gegaard in vet",
        "description": "Een roux is bloem gegaard in vet vóór de vloeistof, in gelijke delen, naar gewicht. Wit, blond of bruin. In het Duits noemt de brigade hem Mehlschwitze.",
        "term": "roux",
        "lead": "De vraag wat is een roux stelt u zodra een saus bloem nodig heeft zonder klonten. U gaart de bloem eerst in vet, in gelijke delen, naar gewicht, vóór de vloeistof erbij komt. Wit, blond of bruin zit in hoe ver u die bloem doorzet. In het Duits heet dit Mehlschwitze, en het is geen beurre manié.",
        "paras": [
            "Een roux is bloem die u gaart in vet voordat er ook maar vloeistof bij komt. De verhouding is gelijke delen, naar gewicht. Het vet draagt de bloem, de bloem verliest haar rauwe smaak, en pas daarna neemt de roux de fond of de melk op. Dat is het verschil met een zetmeelpap en met een beurre manié, waarin de bloem rauw blijft tot het eind. In het Duits heet deze basis Mehlschwitze. De Nederlandse keuken zegt roux. Zonder dat garen in vet blijft de bloem rauw en de saus klontert zodra de fond erbij komt.",
            "Wit, blond en bruin zijn dezelfde techniek, verder of minder ver gegaard. Een witte roux blijft bleek en draagt sauzen die licht moeten ogen. Een blonde krijgt kleur en een geur van gebakken bloem, en past bij fond die zelf ook licht is. Een bruine gaat door tot de kleur diep is en de geur naar gebakken korst neigt. U roert. U laat de pan niet met rust. Aangebrande bloem wordt bitter en redt u niet met extra vet. U blijft erbij, want bloem die aanbrandt geeft een bittere saus die u niet meer redt.",
            "In de mise en place weegt u bloem en vet in gelijke delen, naar gewicht, voordat de service begint. Een scheut op het oog maakt de roux of te vet of te droog, en de saus klontert of scheidt. De chef-kok legt vast welke kleur bij welk gerecht hoort, zodat de brigade niet op de passe nog een bruine roux staat te duwen. De pan is zwaar genoeg om de hitte te verdelen. Een garde of een lepel blijft erin. U zet de pan op tijd van het vuur, anders gaart de kleur door terwijl u de fond pakt.",
            "Op de passe is de roux al klaar. U bouwt hem niet terwijl de gast wacht, tenzij de fiche een noodgeval toestaat en zelfs dan liever een beurre manié. De saus die uit de roux komt, warmt u zacht op. Een vel op de oppervlakte roert u weg voordat het bord gaat. De gast proeft rauwe bloem meteen als de roux te kort gegaard was, en bitter als hij verbrand is. De chef-kok proeft de saus los van het vlees. De saus warmt u zacht op, anders komt er een vel op dat de lepel niet meer glad krijgt.",
            "Een verbrande of rauwe roux raakt de marge omdat de hele saus erop steunt. U gooit dan niet alleen bloem weg, u begint de pan opnieuw terwijl de zaal doorgaat. Gelijke delen, naar gewicht, en aandacht bij het garen, voorkomen dat. Mehlschwitze of roux, de discipline is dezelfde. De fiche noemt de kleur. Zo pakt de mise en place niet de witte pan voor een donker gerecht, en omgekeerd. De kleur op de fiche voorkomt dat u de witte pan pakt voor een donker gerecht, of omgekeerd, terwijl de zaal al loopt.",
        ],
        "busca": "De vraag wat is een roux hoort bij bloem die u in vet gaart, niet bij een pap van rauwe bloem. In het Duits heet dezelfde basis Mehlschwitze, en die schrijfwijze komt voorbij waar Duits en Nederlands in de brigade door elkaar lopen. Wit, blond en bruin zijn een mate van garen, geen andere recepten. Beurre manié zoekt u apart, net als zetmeelpap. U zet roux op de fiche met de kleur erbij, anders warmt de mise en place de verkeerde pan.",
        "rows": [
            ("Bloem in vet", "Eerst garen, dan vloeistof", "Niet rauw in de saus strooien"),
            ("Gelijke delen", "Naar gewicht", "Geen scheut op het oog"),
            ("Wit, blond, bruin", "De kleur volgt het garen", "Geen apart recept per kleur"),
            ("Mehlschwitze", "De Duitse naam voor roux", "Geen andere techniek"),
        ],
        "faq": [
            (
                "Wat is een roux?",
                "Een roux is bloem gegaard in vet, in gelijke delen, naar gewicht, vóór de vloeistof erbij komt. Zo verliest de bloem haar rauwe smaak en kan zij de saus dragen zonder klonten. Wit, blond of bruin hangt af van hoe ver u gaart. In het Duits heet dit Mehlschwitze. Het is geen beurre manié en geen zetmeelpap. Op de passe staat de roux al klaar.",
            ),
            (
                "Wat is een Mehlschwitze?",
                "Mehlschwitze is het Duitse woord voor roux. Bloem gaart in vet voordat de vloeistof komt, in gelijke delen, naar gewicht. Het is geen andere techniek en geen beurre manié. In een brigade waar Duits en Nederlands elkaar raken, staan beide woorden voor dezelfde pan. Op de fiche kiest u één naam en u zet de kleur erbij: wit, blond of bruin.",
            ),
            (
                "Wat verschilt wit, blond en bruin?",
                "Alleen hoe ver u de bloem in het vet gaart. Wit blijft bleek, blond krijgt kleur en geur, bruin gaat dieper en ruikt naar gebakken korst. Het blijven gelijke delen, naar gewicht. U roert en u laat de pan niet aanbranden, want bittere bloem redt u niet. De fiche noemt de kleur bij het gerecht. De gast proeft een te rauwe of een verbrande roux meteen.",
            ),
            (
                "Is een roux een beurre manié?",
                "Nee. In een roux gaart de bloem eerst in vet. In een beurre manié blijft zij rauw en gaat zij pas aan het eind door de saus, ook in gelijke delen, naar gewicht. Wisselt u ze om, dan mist de saus haar basis of proeft de gast bloem. Op de passe zijn het twee momenten. De mise en place zet ze niet in dezelfde pan.",
            ),
        ],
        "alt": [
            "Bloem die in vet gaart in een pan, het begin van een roux",
            "Witte, blonde en bruine roux naast elkaar in de pan",
            "Een saus op basis van roux, glad en zonder klonten, op de passe",
        ],
        "tags": '["roux", "Mehlschwitze", "bloem", "horeca"]',
        "links": [
            ("manie", "Beurre manié: dezelfde delen, maar rauw en aan het eind"),
            ("papilla", "Zetmeelpap bindt zonder de bloem eerst te garen"),
            ("demi", "Demi-glace steunt op een bruine basis, niet op een witte roux"),
        ],
    },
    "emulsion": {
        "title": "Emulsie: twee vloeistoffen die niet mengen",
        "description": "Een emulsie houdt twee vloeistoffen bij elkaar die niet mengen, met eigeel, mosterd of lecithine. Mayonaise, hollandaisesaus en vinaigrette houden niet even goed.",
        "term": "emulsie",
        "lead": "Een emulsie houdt twee vloeistoffen bij elkaar die uit zichzelf niet mengen. Eigeel, mosterd of lecithine doen dat werk in de pan. Mayonaise, hollandaisesaus en vinaigrette zijn alle drie een emulsie, en toch houden ze niet even goed. Op de passe merkt u dat verschil zodra een saus moet wachten op de gast.",
        "paras": [
            "Een emulsie is het samengaan van twee vloeistoffen die elkaar loslaten zodra u stopt met dwingen. Olie en water, boter en een waterige reductie, azijn en olie: zonder hulp scheiden zij. Eigeel, mosterd of lecithine houden de druppels klein en verdeeld. Mayonaise, hollandaisesaus en vinaigrette zijn daardoor familie, en toch niet even stabiel. De ene blijft staan, de andere laat los als zij wacht of te heet wordt. De naam emulsie zegt nog niet hoe lang de saus meegaat. Hoe lang de saus blijft staan, hangt af van wat haar vasthoudt, niet van het woord emulsie alleen.",
            "Mayonaise bouwt u koud. Het eigeel of de mosterd pakt de olie beetje bij beetje, en de saus blijft daarna staan als u haar koel en afgedekt bewaart. Hollandaisesaus is warm. Boter gaat door eigeel, weg van een harde kook, en de emulsie is prachtig en kwetsbaar. Een vinaigrette klopt u snel. Zij glanst even en scheidt weer als zij blijft staan, omdat weinig haar vasthoudt. U behandelt ze niet met dezelfde haast en niet met hetzelfde vuur. U geeft de vinaigrette een laatste klop en u laat de mayonaise met rust zolang zij glanst.",
            "In de mise en place staan eigeel, mosterd en olie koud, en de boter voor de hollandaisesaus ook koud tot u haar smelt of monteert. De kom is droog voor de koude saus en warm voor de warme. De chef-kok zet de vinaigrette apart van de mayonaise, zodat niemand een losse dressing als stabiele saus de passe op stuurt. Lecithine zit in het eigeel, u hoeft er geen zak van te zoeken als het ei er al is. De fiche noemt welk houvast de saus gebruikt.",
            "Op de passe merkt de gast een gebroken emulsie eerder dan u soms wilt. Een doorgeslagen mayonaise oogt als olie met vlokken. Een hollandaisesaus die te heet werd, schift in boter en ei. Een vinaigrette die u te vroeg klopte, staat in twee lagen op de sla. U geeft de stabiele saus uit zolang zij glanst, en u klopt de vinaigrette op het laatste moment. De chef-kok redt een begin van schiften alleen als de saus het nog pakt, niet als het bord al weg is.",
            "Elke gebroken pan raakt de marge. Olie, boter en eigeel zijn dan vaak niet meer het bord waard, en de service staat. U voorkomt dat door de saus te kiezen bij de tijd die zij krijgt. Mayonaise kan wachten, hollandaisesaus nauwelijks, vinaigrette eigenlijk niet. De fiche zegt dat hardop. Zo grijpt de brigade niet naar één woord emulsie alsof alle drie de sauzen hetzelfde geduld hebben. U plant de warme saus bij de uitgifte en de koude saus in de koeling, niet allebei op dezelfde plek van de passe.",
        ],
        "busca": "Emulsie is het woord dat de Nederlandse kok intikt. U zoekt het als mayonaise, hollandaisesaus of vinaigrette uit elkaar valt of juist blijft staan. Eigeel, mosterd en lecithine zijn de woorden die erbij horen. Een vinaigrette zoekt u niet met hetzelfde vertrouwen als een mayonaise: de ene houdt, de andere laat los. U schrijft emulsie bij de techniek en de sausnaam bij het recept, anders raakt de fiche in de war op de passe.",
        "rows": [
            ("Twee vloeistoffen", "Blijven samen door een hulp", "Mengen niet uit zichzelf"),
            ("Eigeel, mosterd, lecithine", "Houden de druppels klein", "Zijn geen smaak op zich alleen"),
            ("Mayonaise", "Koud en stabiel", "Is geen warme botersaus"),
            ("Vinaigrette", "Houdt kort", "Wacht niet als een mayonaise"),
        ],
        "faq": [
            (
                "Wat is een emulsie?",
                "Een emulsie houdt twee vloeistoffen bij elkaar die niet mengen, zoals olie en een waterige vloeistof of boter en een reductie. Eigeel, mosterd of lecithine doen dat werk. Zonder die hulp scheiden de vloeistoffen weer. Mayonaise, hollandaisesaus en vinaigrette zijn emulsies, maar zij houden niet even lang. Op de passe plant u de saus bij haar geduld, niet bij het woord alleen.",
            ),
            (
                "Waarom houden mayonaise en vinaigrette niet even goed?",
                "Mayonaise heeft eigeel of mosterd die de olie vasthoudt, en zij blijft staan als u haar koud bewaart. Een vinaigrette klopt u snel en zij scheidt weer, omdat weinig haar bij elkaar houdt. Hollandaisesaus zit ertussenin: warm, glanzend en kwetsbaar voor hitte. De gast ziet een gebroken saus meteen. Op de fiche behandelt u ze als familie, niet als dezelfde pan.",
            ),
            (
                "Wat houdt de emulsie bij elkaar?",
                "Eigeel, mosterd of lecithine. Het eigeel brengt lecithine mee, mosterd helpt vooral bij een vinaigrette of een mayonaise, en zonder zo'n hulp vallen olie en water uit elkaar. U voegt de olie of de boter geleidelijk toe terwijl u klopt. Een harde kook breekt de warme emulsie. In de mise en place staat die hulp klaar voordat de olie stroomt.",
            ),
            (
                "Is een hollandaisesaus een emulsie?",
                "Ja. Boter en de waterige kant van het eigeel blijven samen zolang u de saus warm houdt zonder haar te laten koken. Zij is kwetsbaarder dan mayonaise en stabieler dan een vinaigrette die u laat staan. Schift zij, dan ziet de gast boter en ei apart. Op de passe maakt u haar dicht bij het uitgeven. De fiche noemt haar emulsie en noemt het gevaar erbij.",
            ),
        ],
        "alt": [
            "Olie die langzaam door eigeel wordt geklopt tot een samenhangende mayonaise",
            "Een hollandaisesaus die glanst in een kom, weg van een harde kook",
            "Een vinaigrette die net geklopt is en nog niet opnieuw uiteenvalt",
        ],
        "tags": '["emulsie", "mayonaise", "hollandaisesaus", "horeca"]',
        "links": [
            ("yema", "Liaison met eigeel: binden, geen boteremulsie"),
            ("blanc", "Beurre blanc, een instabiele emulsie zonder eigeel"),
            ("montar", "Monteren met boter, glans aan het eind van een saus"),
        ],
    },
    "demi": {
        "title": "Demi-glace: Spaanse saus en bruine fond",
        "description": "Demi-glace is Spaanse saus plus bruine fond, gereduceerd tot hij nappeert. Schrijfwijzen: demi-glace, demi glace en demiglace. Het is niet de vleesglace.",
        "term": "demi-glace",
        "lead": "Demi-glace is Spaanse saus plus bruine fond, samen gereduceerd tot de saus nappeert. U schrijft demi-glace, demi glace of demiglace, en u bedoelt hetzelfde. Het is niet de vleesglace: die kookt u verder in, tot hij koud geleert. Op de passe is demi-glace de saus die aan het vlees blijft, niet een gelei in de lepel.",
        "paras": [
            "Demi-glace is de ontmoeting van Spaanse saus en bruine fond. U zet ze samen en u reduceert tot de saus de achterkant van de lepel bedekt. Dan nappeert hij. De schrijfwijze wisselt: demi-glace, demi glace of demiglace, en het blijft dezelfde saus. Het is niet de vleesglace. Die gaat verder, tot de reductie koud geleert. Een demi-glace blijft een saus die u kunt napperen en uitschenken, geen gelei die u in een pot snijdt. U schenkt hem uit als saus. Een gelei die u moet snijden, heeft u te ver doorgetrokken.",
            "U reduceert zacht en u schept af wat de saus troebel maakt. Een harde kook jaagt hem tegen de rand en geeft een bittere zoom. De lepel is de maat, niet een gevoel van hoe lang de pan al staat. Nappeert hij, dan proeft u. Te zout betekent dat u te ver bent gegaan voor deze saus en richting glace beweegt. Te dun betekent dat de fond nog te veel ruimte inneemt. U corrigeert met geduld, niet met een schep zetmeel die de glans dooft.",
            "In de mise en place staan Spaanse saus en bruine fond als twee potten, gelabeld, niet als één anonieme bruine emmer. De chef-kok wil dat de brigade demi-glace pas schrijft als de reductie nappeert. Een fond die u alleen heeft opgewarmd, is nog geen demi-glace, welke schrijfwijze er ook op het etiket stond. U koelt wat overblijft afgedekt. Op de pot staat één schrijfwijze, dezelfde als op de fiche, zodat de passe niet hoeft te vertalen. Een fond die u alleen opwarmt, schrijft u niet om tot demi-glace omdat het etiket dat handig vindt.",
            "Op de passe draagt demi-glace het vlees. De gast ziet een saus die blijft liggen en proeft fond, niet een waterige plas en niet een zoute gelei. U warmt hem zacht op. Een vel roert u weg. U monteert desnoods met een weinig koude boter voor de glans, zonder er een andere saus van te maken. De chef-kok test de lepel voordat de serie borden gaat. Een pan die niet nappeert, gaat niet de zaal in. De laag op het vlees is wat de gast ziet, en een waterige plas stuurt u niet de zaal in.",
            "Verwart u demi-glace met vleesglace, dan raakt dat de marge aan twee kanten. Te ver reduceren levert een gelei waar de kaart een saus beloofde, en de fond is op. Te vroeg stoppen levert een dunne jus en een bord dat terugkomt. De fiche noemt Spaanse saus, bruine fond en de lepeltest, en zij noemt de vleesglace als een andere pot. Zo blijft de brigade stoppen op nappé, niet op gelei. U labelt de pot op het moment dat de lepel slaagt, niet eerder, anders groeit de naam sneller dan de saus.",
        ],
        "busca": "Demi-glace, demi glace en demiglace zijn schrijfwijzen van dezelfde saus, niet verschillende recepten. De kok die het streepje weglaat, zoekt hetzelfde als de kok die het aan elkaar schrijft. Het blijft Spaanse saus plus bruine fond, ingekookt tot hij nappeert. Vleesglace en glace de viande gaan verder en horen niet in dezelfde pot. U zet op het etiket de schrijfwijze die uw fiche gebruikt, en u gebruikt die ook op de passe.",
        "rows": [
            ("Spaanse saus plus fond", "Samen reduceren", "Niet alleen opgewarmde fond"),
            ("Tot hij nappeert", "De lepel blijft bedekt", "Niet door tot gelei"),
            ("Schrijfwijzen", "Demi-glace, demi glace, demiglace", "Geen drie verschillende sauzen"),
            ("Niet de vleesglace", "Die geleert als hij koud is", "Andere pot, andere diepte"),
        ],
        "faq": [
            (
                "Wat is een demi-glace?",
                "Demi-glace is Spaanse saus plus bruine fond, samen gereduceerd tot de saus nappeert. Hij bedekt de achterkant van de lepel en blijft een saus. Het is niet de vleesglace, die u verder inkookt tot hij koud geleert. Op de passe draagt hij het vlees. De gast ziet een laag die blijft liggen, geen plas en geen gelei. De fiche noemt beide potten apart.",
            ),
            (
                "Hoe schrijft u demi-glace?",
                "Als demi-glace, als demi glace of als demiglace. Het zijn schrijfwijzen, geen verschillende recepten. Op de fiche en op de pot kiest u er één en u houdt die aan. Zoekt iemand de andere vorm, dan bedoelt hij dezelfde saus. Vleesglace en glace de viande horen niet in dat rijtje. Die naam betekent een verdere reductie. De passe raakt in de war van wisselende etiketten.",
            ),
            (
                "Is demi-glace hetzelfde als vleesglace?",
                "Nee. Demi-glace nappeert en blijft uitschenkbaar. Vleesglace, de glace de viande, gaat verder tot hij koud geleert. Gebruikt u de glace waar de kaart demi-glace bedoelt, dan wordt het bord te zwaar en te zout. Andersom blijft de saus te dun. In de mise en place zijn het twee potten. De chef-kok proeft het verschil zonder op het etiket te hoeven vertrouwen.",
            ),
            (
                "Wanneer nappeert een demi-glace?",
                "Als een lepel door de saus een gesloten laag op de achterkant houdt. Loopt het metaal bloot, dan is hij nog te dun en reduceert u verder, zacht. Geleert een afgekoelde lepel als een stijve gelei, dan bent u voorbij demi-glace en in de vleesglace. U stopt op de saus, niet op de gelei. Op de passe test u opnieuw na het opwarmen.",
            ),
        ],
        "alt": [
            "Spaanse saus en bruine fond samen in een pan, zacht aan het reduceren",
            "Een lepel demi-glace waarvan de achterkant bedekt blijft",
            "Demi-glace bij het vlees op de passe, glanzend en niet geleiachtig",
        ],
        "tags": '["demi-glace", "demi glace", "demiglace", "horeca"]',
        "links": [
            ("glace", "Vleesglace gaat verder en geleert als hij koud is"),
            ("napar", "Napperen is de test waarop deze saus stopt"),
            ("roux", "De roux onder de bruine saus, niet de reductie zelf"),
        ],
    },
}
