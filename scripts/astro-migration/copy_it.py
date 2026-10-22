# -*- coding: utf-8 -*-
"""Copy italiana del glosario de salsas (tanda 1). Registro: tu.

Doce fichas. Hechos de partida, sin cifras de receta. La proporción «a parti
uguali, a peso» vive solo en beurre manié y roux.
"""
from __future__ import annotations

COPY = {
    "manie": {
        "title": "Beurre manié: burro e farina a crudo, a fine cottura",
        "description": (
            "Il beurre manié è burro morbido e farina a parti uguali, a peso, "
            "lavorati a crudo. Lo sbricioli a fine cottura per legare. Non è un roux cotto."
        ),
        "term": "Beurre manié",
        "lead": (
            "Il beurre manié lega un liquido già quasi pronto, senza rifare la salsa. "
            "Lavori burro morbido e farina a parti uguali, a peso, e li lasci crudi. "
            "Lo sbricioli a fine cottura, fuori dal bollore pieno. Non è un roux: "
            "la farina non ha cotto nel grasso prima del liquido. Sul passe recuperi "
            "un fondo troppo lento."
        ),
        "paras": [
            (
                "La mise en place del beurre manié è una pallina, non una salsa già "
                "scritta in carta. Prendi burro che cede sotto il pollice, né fuso "
                "né ghiacciato, e lavoralo con la farina a parti uguali, a peso, "
                "finché sul tagliere non resta polvere bianca. Lo tieni crudo. Non "
                "lo tosti, non lo biondi, non aspetti un profumo di biscotto: quel "
                "passaggio appartiene al roux, e se lo fai hai cambiato gesto. La "
                "pallina resta coperta, in un contenitore della partita, pronta per "
                "il momento in cui un liquido arriva corto di corpo. È un attrezzo "
                "di linea, non un nome da menu."
            ),
            (
                "Lo usi quando la cottura è già fatta e manca solo il corpo. Un "
                "brasato, un fondo, un ragù di servizio che al cucchiaio scappa "
                "troppo veloce: sbricioli la pallina fuori dal bollore pieno e la "
                "sbatti nel liquido che sobbolle appena. L'amido della farina si "
                "apre lì, a contatto col caldo, e il burro aiuta a disperderlo "
                "senza grumi. Se butti la pallina in un bollore violento, la farina "
                "si chiude in palline dure e il commensale le trova. Tieni la "
                "pentola docile, gira con la frusta, e assaggia: se senti farina "
                "cruda, non hai dato tempo all'amido."
            ),
            (
                "Non confonderlo col roux e non confonderlo col mantecare. Nel roux "
                "la farina cuoce nel grasso prima che arrivi qualsiasi liquido, e "
                "da quel colore nascono bianco, biondo e bruno. Qui la farina resta "
                "cruda fino all'ultimo e incontra il liquido già caldo. Mantecare, "
                "o monter au beurre, è burro freddo sbattuto in una salsa calda, "
                "senza farina: lucida, non addensa con l'amido. La sospensione di "
                "amido non porta burro e spegne la luce. Il beurre manié sta in "
                "mezzo a questi gesti solo se lo racconti male. Se lo racconti "
                "bene, è una cosa sola: grasso e farina crudi, a fine cottura."
            ),
            (
                "Il passe non ti lascia il tempo di partire da un roux. La comanda "
                "è fuori, la salsa è lenta, e la pallina è l'unica cosa già pronta "
                "dentro la mise en place che puoi usare in un gesto. La sbatti, "
                "la lasci prendere, la guardi sul "
                "dorso del cucchiaio. Se copre, puoi mandare. Se ancora scorre come "
                "acqua, ne sbricioli ancora un poco e aspetti, sempre fuori dal "
                "bollore pieno. Il commensale non sa come si chiama il gesto. Sa "
                "se la salsa veste la carne o se la abbandona nel piatto. Il tuo "
                "lavoro è che non debba chiederselo."
            ),
            (
                "Il margine si difende qui in un modo molto concreto: non ributti "
                "una cottura lunga solo perché è arrivata magra. Recuperi il corpo "
                "con qualcosa che avevi già lavorato a crudo, senza aprire un'altra "
                "pentola e senza cambiare il sapore con una tostatura che il piatto "
                "non chiedeva. Il rischio, se esageri, è una salsa pastosa, opaca, "
                "con la farina ancora in bocca. Allora ti fermi prima. Meglio un "
                "velo corto e pulito che un muro di amido. Da capo cuoco lo tieni "
                "in conto come rete di sicurezza, non come abitudine per coprire "
                "un fondo fatto male ogni sera."
            ),
        ],
        "busca": (
            "In brigata e nel cercarlo lo scrivi beurre manié, con l'accento, e "
            "spesso anche beurre manie, senza accento, perché la tastiera del "
            "passe non aspetta. Non cercarlo come roux: il roux cuoce la farina "
            "nel grasso prima del liquido, questa pallina no. Non è mantecare e "
            "non è il burro bianco. È farina cruda e burro morbido, a fine "
            "cottura, per dare corpo a un liquido già nato. Se cerchi una salsa "
            "con un nome di carta, sei nel gesto sbagliato."
        ),
        "rows": [
            ("Beurre manié", "Lega a crudo, a fine cottura", "Non tosta la farina"),
            ("Roux", "Cuoci farina e grasso prima", "Non è una pallina cruda"),
            ("Mantecare", "Monta burro freddo, senza farina", "Non addensa con l'amido"),
            ("Amido sciolto", "Sospendi l'amido a freddo", "Non porta burro nel gesto"),
        ],
        "faq": [
            (
                "Il beurre manié è un roux?",
                "No. Il roux cuoce la farina nel grasso prima che tu versi il liquido, "
                "e da quella cottura nascono il bianco, il biondo e il bruno. Il beurre "
                "manié resta crudo: burro morbido e farina lavorati insieme, poi "
                "sbriciolati a fine cottura. Se lo tosti, hai cambiato gesto e non "
                "stai più legando all'ultimo momento.",
            ),
            (
                "Quando lo aggiungi?",
                "A fine cottura, quando il liquido è già pronto e ti manca solo il "
                "corpo. Lo sbricioli fuori dal bollore pieno e lo sbatti nel liquido "
                "che sobbolle appena. Se lo butti in un bollore violento, la farina "
                "si chiude in grumi. Poi assaggi: la farina cruda in bocca ti dice "
                "che non hai lasciato aprire l'amido.",
            ),
            (
                "Perché burro e farina vanno insieme?",
                "Perché il burro morbido bagna la farina e te la tiene dispersa, così "
                "quando la sbricioli nel liquido caldo non fa palle secche. Li lavori "
                "a parti uguali, a peso, e li lasci crudi. Non è una misura da "
                "laboratorio: è la definizione del gesto. Se manca burro, la farina "
                "resta polvere. Se manca farina, stai solo montando burro.",
            ),
            (
                "Si può usare al posto del mantecare?",
                "No, sono due chiusure diverse. Mantecare è burro freddo sbattuto in "
                "una salsa calda, senza farina: lucida e non addensa con l'amido. Il "
                "beurre manié porta farina cruda e serve quando ti manca corpo, non "
                "quando ti manca solo luce. Se la salsa è già nappante e vuoi solo "
                "seta, monta il burro e lascia stare la pallina.",
            ),
        ],
        "alt": [
            "Pallina di beurre manié, burro morbido e farina ancora crudi, sul tagliere della partita",
            "Beurre manié sbriciolato in un fondo che sobbolle appena, con la frusta in mano",
            "Salsa legata a fine cottura, velata sul dorso del cucchiaio, accanto alla pallina cruda",
        ],
        "tags": '["beurre manié", "legatura", "salse", "tecnica di cucina"]',
        "links": [
            ("roux", "il roux, che cuoce la farina"),
            ("papilla", "la sospensione di amido"),
            ("montar", "mantecare a fine cottura"),
        ],
    },
    "napar": {
        "title": "Nappante: la prova del cucchiaio, non una salsa",
        "description": (
            "Nappante vuol dire che la salsa copre il dorso del cucchiaio e resta. "
            "È una prova di cottura, non una salsa con un nome suo da scrivere in carta."
        ),
        "term": "Nappante",
        "lead": (
            "Nappante è una prova, non una salsa. Immergi il cucchiaio e guardi "
            "il dorso: la salsa lo copre e non scappa come acqua. In brigata il "
            "verbo è napper. Non ha un nome di carta e non si ordina. Ti dice "
            "solo se la pentola è pronta oppure è ancora un liquido."
        ),
        "paras": [
            (
                "La mise en place non ti consegna una ciotola etichettata nappante. "
                "Ti consegna salse, fondi, riduzioni, e tu a un certo punto devi "
                "decidere se sono pronte. La decisione sta nel cucchiaio. Lo "
                "immergi, lo sollevi di taglio, e guardi se il liquido veste il "
                "dorso o se lo lascia nudo subito. Se lo copre e resta, "
                "dici che è nappante. Se scorre via e il metallo ritorna lucido e "
                "vuoto, non lo è. Non c'è un'altra salsa nascosta dietro questa "
                "parola. C'è solo un sì o un no, detto con la mano."
            ),
            (
                "Napper, il verbo che passa di bocca in bocca in cucina, è lo "
                "stesso giudizio. Napper una carne vuol dire coprirla con una "
                "salsa che tiene, non annegarla. Napper il cucchiaio vuol dire "
                "che quella salsa ha il corpo giusto per farlo. Le due frasi si "
                "tengono: se non nappa il cucchiaio, non napperai il piatto, "
                "farai una pozza. Sul servizio questo ti salva dalle discussioni "
                "inutili. Non chiedi a un compagno se «è abbastanza». Gli fai "
                "vedere il dorso. La prova è pubblica, si guarda in due, e chiude "
                "la chiacchiera."
            ),
            (
                "La gente cerca «salsa nappante» come se fosse una ricetta madre, "
                "sorella della spagnola o del burro bianco. Non lo è. Una "
                "demi-glace può essere nappante. Una glace pure, quando è ancora "
                "abbastanza morbida da velare. Un'emulsione può coprire il "
                "cucchiaio e però rompersi dopo, perché la tenuta di un'emulsione "
                "non è la tenuta di una riduzione. Il giudizio nappante non ti "
                "dice di che salsa si tratta. Ti dice solo che, in questo "
                "momento, il corpo c'è. Confondere la prova col nome è il modo "
                "più rapido di imparare la parola e non il gesto."
            ),
            (
                "Il passe usa la prova come filtro. La salsa esce dalla "
                "pentola e, prima di toccare il piatto, qualcuno guarda il "
                "cucchiaio. Se non copre, non parte: o riduci ancora, o leghi "
                "con il gesto che il piatto sopporta, e poi ricontrolli. Il "
                "commensale vede il risultato, non il cucchiaio. Vede una carne "
                "vestita oppure una carne seduta in un brodo chiaro che non "
                "avevi promesso. Tra i due piatti c'è questa prova, fatta in "
                "silenzio, ogni volta, anche quando la sala preme e la mano "
                "vorrebbe spedire lo stesso."
            ),
            (
                "Il margine entra nella prova perché una salsa che non nappa ti "
                "costringe a scegliere. O la tieni ancora sul fuoco, e il passe "
                "aspetta, o la mandi corta e il piatto torna indietro. Nessuna "
                "delle due strade è gratis in tempo di brigata. Imparare a "
                "leggere il dorso del cucchiaio ti evita di ridurre per abitudine "
                "fino a un estratto che il piatto non chiedeva, e ti evita anche "
                "di spedire acqua legata col nome di una salsa. La mise en place "
                "può essere perfetta: se all'ultimo non fai la prova, il commensale "
                "mangia la tua fretta."
            ),
        ],
        "busca": (
            "Lo cerchi come nappante, aggettivo, e come napper, il verbo francese "
            "che in brigata vuol dire coprire. Non è il nome di una salsa. Una "
            "salsa è nappante quando veste il dorso del cucchiaio e ci resta. "
            "La demi-glace, la glace, un fondo ridotto possono esserlo: la parola "
            "giudica il corpo, non la ricetta. Se cerchi «salsa nappante» come "
            "voce di menu, stai cercando una prova e le hai dato un nome che non ha."
        ),
        "rows": [
            ("Nappante", "La salsa veste il cucchiaio", "Non è una salsa con un nome"),
            ("Napper", "Copri il pezzo, non lo anneghi", "Non è un altro preparato"),
            ("Riduzione", "Può arrivare a nappare", "Non ogni riduzione è già pronta"),
            ("Emulsione", "Può coprire e poi rompersi", "La prova non garantisce la tenuta"),
        ],
        "faq": [
            (
                "Nappante è una salsa?",
                "No. È la prova con cui decidi se una salsa è pronta. Immergi il "
                "cucchiaio, lo sollevi e guardi il dorso: se la salsa lo copre e "
                "resta, è nappante. Se scorre via, è ancora un liquido. Non si "
                "scrive in carta e non si ordina. Si usa per chiudere una cottura "
                "prima che il piatto esca.",
            ),
            (
                "Che differenza c'è tra nappante e napper?",
                "Nappante è l'aggettivo: la salsa è nappante quando veste il dorso "
                "del cucchiaio. Napper è il verbo che senti in brigata, spesso "
                "lasciato in francese: napper il cucchiaio, napper la carne. È lo "
                "stesso gesto visto da due lati. Non sono due ricette e non sono "
                "due salse diverse.",
            ),
            (
                "Una salsa lucida è sempre nappante?",
                "No. La luce può venire dal burro montato a fine cottura, e il "
                "corpo da una riduzione o da una legatura. Puoi avere una salsa "
                "lucida che ancora scorre via dal cucchiaio, e una salsa coprente "
                "che è opaca. Guardi il dorso, non il riflesso. Il riflesso dice "
                "un'altra cosa, non questa prova.",
            ),
            (
                "La demi-glace è la salsa nappante?",
                "La demi-glace, quando è fatta, nappa: salsa spagnola e fondo bruno "
                "ridotti finché coprono il cucchiaio. Questo non trasforma "
                "«nappante» nel suo nome. Anche una glace, finché è abbastanza "
                "morbida da velare, supera la stessa prova, ed è un altro grado "
                "di riduzione. La prova è una. Le salse sono tante.",
            ),
        ],
        "alt": [
            "Cucchiaio sollevato da una salsa che ne copre il dorso e non scorre via",
            "Mano che controlla il punto nappante prima di vestire la carne al passe",
            "Piatto con la salsa che copre la carne, accanto al cucchiaio della prova",
        ],
        "tags": '["nappante", "napper", "salse", "tecnica di cucina"]',
        "links": [
            ("demi", "la demi-glace, quando nappa"),
            ("glace", "la glace de viande"),
            ("emulsion", "un'emulsione e la sua tenuta"),
        ],
    },
    "montar": {
        "title": "Mantecare: monter au beurre, il burro freddo a fine cottura",
        "description": (
            "Mantecare, o monter au beurre, è burro freddo sbattuto in una salsa "
            "calda, fuori dal bollore pieno. Non è il burro bianco né il beurre manié."
        ),
        "term": "Mantecare",
        "lead": (
            "Mantecare è burro freddo sbattuto in una salsa calda, a fine cottura, "
            "fuori dal bollore pieno. In francese è monter au beurre. Senza farina: "
            "luce, non amido. Non è il burro bianco, che è una salsa intera, e non "
            "è il beurre manié. È solo la chiusura."
        ),
        "paras": [
            (
                "La mise en place di questo gesto è semplice e si dimentica lo "
                "stesso: burro freddo, a cubetti, già tagliato, non il panetto "
                "intero da aggredire quando la comanda urla. Lo tieni al freddo "
                "della partita. La salsa, nel frattempo, è calda ma non in "
                "ebollizione piena. Se bolle forte, il burro si separa e tu "
                "insegui una salsa rotta con altra frusta. Abbassi, aspetti che "
                "il bollore ceda, e solo allora sbatti il burro freddo dentro, "
                "un pezzo dopo l'altro, finché la superficie prende quella luce "
                "che il liquido da solo non aveva."
            ),
            (
                "Nel risotto, mantecare è lo stesso gesto di montare con grasso "
                "a fine cottura. Lo dici così perché in Italia la parola la "
                "impari lì, a fine cottura, fuori dal bollore, per legare e "
                "lucidare. Non è una ricetta di risotto e non diventa un "
                "capitolo di riso: è il medesimo montare. Il grasso freddo entra "
                "quando la cottura è finita, non mentre il liquido salta. Se lo "
                "tratti come un condimento buttato a caso nel bollore, non "
                "mantechi: sciogli burro e lo lasci andare. Il gesto chiede "
                "frusta, o un movimento deciso, e una pentola che non urla."
            ),
            (
                "Non è il burro bianco. Il burro bianco parte da una riduzione "
                "di scalogno, vino bianco e aceto, e solo alla fine usa questo "
                "montare. La salsa intera ha un nome. Il gesto, da solo, si "
                "chiama mantecare o monter au beurre, e lo fai su una riduzione "
                "di carne, su un fondo, su un succo già pulito. Non è neanche il "
                "beurre manié: lì c'è farina cruda, e cerchi corpo di amido, non "
                "luce di burro. Se la salsa è magra di corpo, la pallina di "
                "farina e burro fa un altro lavoro. Se la salsa ha già corpo e "
                "ti manca seta, monti burro e basta."
            ),
            (
                "Il passe non perdona l'attesa del burro montato. Una salsa "
                "mantecata sta bene nel breve, poi la luce cade, il burro può "
                "riaffiorare, e se la rimetti su un bollore pieno la perdi. Per "
                "questo mantechi quando il piatto è davvero in uscita, non "
                "prima per «andare avanti». Il commensale vede una salsa che "
                "avvolge e riflette, oppure una salsa smunta con chiazze di "
                "grasso. Non sa il nome francese. Sa se il cucchiaio scorre "
                "setoso o se il piatto è unto. La differenza la fai tu negli "
                "ultimi istanti, con il burro ancora freddo."
            ),
            (
                "Il margine di questo gesto è il burro che metti e il piatto che "
                "non torna. Montare chiede grasso buono: se lo fai su una salsa "
                "già rotta, o su un liquido che non aveva corpo né pulizia, "
                "stai coprendo un errore con altro burro e il commensale lo sente "
                "lo stesso. Usalo quando la riduzione è già giusta e manca solo "
                "la chiusura. La mise en place del burro freddo ti evita di "
                "tagliare il panetto col passe addosso, che è il modo in cui la "
                "scaldi troppo e perdi il piatto. Gesto "
                "corto, fatto tardi, fatto bene."
            ),
        ],
        "busca": (
            "In Italia lo cerchi mantecare, ed è la parola giusta anche fuori "
            "dal risotto: grasso a fine cottura. In francese è monter au beurre, "
            "lo stesso sbattere burro freddo in una salsa calda, fuori "
            "dall'ebollizione piena. Non cercarlo come burro bianco e non "
            "cercarlo come beurre manié. Il burro bianco è la salsa con la "
            "riduzione. Il beurre manié porta farina. Mantecare è solo la "
            "chiusura, la luce, il gesto ultimo."
        ),
        "rows": [
            ("Mantecare", "Burro freddo in salsa calda", "Non porta farina"),
            ("Burro bianco", "Riduzione, poi il montare", "Non è il gesto da solo"),
            ("Beurre manié", "Farina cruda e burro", "Non lucida senza amido"),
            ("Nel risotto", "Stesso grasso a fine cottura", "Non è una ricetta di riso"),
        ],
        "faq": [
            (
                "Mantecare e monter au beurre sono la stessa cosa?",
                "Sì, è lo stesso gesto con due nomi. Mantecare è la parola che "
                "usi in Italia. Monter au beurre è il francese che senti ancora "
                "in brigata. In tutti e due i casi sbatti burro freddo in una "
                "salsa calda, fuori dal bollore pieno, per legarla e lucidarla. "
                "Non c'è farina. Non è una salsa a sé.",
            ),
            (
                "Si manteca anche il risotto?",
                "Sì, e non è un'altra tecnica. Nel risotto mantecare è lo stesso "
                "montare con grasso a fine cottura, fuori dal bollore, per legare "
                "e lucidare. Non trasformare la parola in una ricetta di riso: "
                "il gesto è uno, e lo fai anche su una salsa o su un succo. Il "
                "riso è solo il posto dove molti cuochi italiani imparano il nome.",
            ),
            (
                "Il burro deve essere freddo?",
                "Sì. Il freddo ti dà il tempo di emulsionare il grasso nella salsa "
                "calda prima che si separi. Se il burro è già fuso, lo versi e "
                "galleggia. Se la salsa bolle piena, il grasso si rompe lo stesso. "
                "Togli dal bollore violento, sbatti il burro freddo, e manda il "
                "piatto mentre la luce tiene.",
            ),
            (
                "Mantecare è fare il burro bianco?",
                "No. Il burro bianco è una salsa: riduzione di scalogno, vino "
                "bianco e aceto, poi burro freddo montato sopra. Quel finale usa "
                "il monter au beurre, ma il nome della salsa non è il gesto. "
                "Mantecare lo fai anche su un fondo di carne, senza scalogno e "
                "senza aceto. Non scambiare la chiusura con la ricetta intera.",
            ),
        ],
        "alt": [
            "Burro freddo a cubetti accanto a una salsa calda, pronto per mantecare",
            "Frusta che sbatte burro freddo in una riduzione fuori dal bollore pieno",
            "Salsa lucida appena mantecata, versata sul piatto al passe",
        ],
        "tags": '["mantecare", "monter au beurre", "salse", "tecnica di cucina"]',
        "links": [
            ("blanc", "il burro bianco"),
            ("manie", "il beurre manié"),
            ("yema", "il legante al tuorlo"),
        ],
    },
    "blanc": {
        "title": "Burro bianco: riduzione di scalogno, vino e aceto, poi burro",
        "description": (
            "Il burro bianco è una riduzione di scalogno, vino bianco e aceto "
            "montata con burro freddo. È un'emulsione instabile: non la ribolli "
            "e non la tieni in attesa."
        ),
        "term": "Burro bianco",
        "lead": (
            "Il burro bianco è una riduzione di scalogno, vino bianco e aceto, "
            "montata con burro freddo. In francese è beurre blanc. È un'emulsione "
            "instabile: sta insieme se la tieni calda e ferma, e si rompe se "
            "bolle. Non è un fondo e non è una maionese. È corta di vita sul servizio."
        ),
        "paras": [
            (
                "La mise en place parte dallo scalogno già tagliato, dal vino "
                "bianco e dall'aceto, non dal burro. Sfumare lo scalogno con "
                "quel liquido è l'inizio: fai partire l'acido e il dolce dello "
                "scalogno, poi riduci finché in pentola resta un liquido corto, "
                "profumato, non una pozza da allungare dopo. Solo allora monti "
                "il burro freddo, fuori dal bollore pieno, come quando mantechi. "
                "Se salti la riduzione e butti il burro in un vino ancora lungo, "
                "non hai un burro bianco: hai burro che galleggia su un liquido "
                "che non ha deciso che salsa essere."
            ),
            (
                "Il montare è lo stesso gesto del monter au beurre, e però la "
                "salsa non si chiama così. Qui il burro entra in una base già "
                "acida e ridotta, e costruisce un'emulsione. Il tuorlo non c'è. "
                "La senape non è il perno, anche se qualcuno la usa per aiutare "
                "la tenuta: il cuore resta burro, scalogno, vino, aceto. "
                "L'emulsione è instabile per natura. Non ha la tenuta di una "
                "maionese e non ha la cottura di un roux. Vive nel breve. La "
                "tratti come una salsa che aspetti al passe, non come una "
                "preparazione che fai al mattino e dimentichi."
            ),
            (
                "Non è il beurre manié e non è la gastrique. Il beurre manié "
                "porta farina cruda e cerca corpo, non questa seta acida. La "
                "gastrique è caramello allentato con aceto: un acido dolce e "
                "scuro, senza burro montato, e non è un'emulsione. Il burro "
                "bianco usa l'aceto dentro una riduzione chiara, poi si veste "
                "di burro. Se lo scurissi con un caramello, staresti facendo "
                "un'altra salsa e le toglieresti il colore che il nome promette. "
                "Tienilo chiaro. L'acido deve restare sveglio, non cotto fino "
                "a scomparire sotto il grasso."
            ),
            (
                "Il passe vede il burro bianco rompersi in due modi, e li "
                "conosci tutti e due. O lo lasci raffreddare e il burro si "
                "riaddensa a chiazze, o lo riporti a bollore e l'emulsione "
                "cede. Non lo ribolli per «rianimarlo». Se si è rotto, a volte "
                "lo riprendi con un poco della sua stessa riduzione calda e "
                "una frusta, fuori dal bollore, ma non è un miracolo garantito. "
                "Il commensale se lo trovi spezzato lo legge subito: grasso da "
                "una parte, liquido dall'altra, scalogno che non lega più nulla. "
                "Meglio una porzione corta, fatta quando il pesce è nel piatto."
            ),
            (
                "Il margine di questa salsa è tutto nel burro che monti e nel "
                "piatto che non rifai. Se la prepari per tutta la sera e la "
                "tieni in un angolo caldo, a servizio avviato è già un'altra cosa, "
                "e tu la butti o la mandi stanca. Costa meno in nervi farne "
                "poca, legata alla comanda, con lo scalogno già sfumato in "
                "mise en place e il burro freddo pronto. Il commensale del "
                "pesce cerca quella nota acida e pulita, non un sugo lungo. "
                "Se la salsa è instabile, il servizio si organizza intorno "
                "alla sua vita corta, non il contrario."
            ),
        ],
        "busca": (
            "Lo cerchi burro bianco, in italiano, e beurre blanc, in francese: "
            "stessa salsa. Non confonderlo con mantecare o con monter au beurre, "
            "che è solo il gesto finale del burro freddo. Qui prima c'è la "
            "riduzione di scalogno, vino bianco e aceto. È un'emulsione "
            "instabile: non la ribolli e non la tratti come una maionese. Se "
            "cerchi una salsa chiara, acida, montata al passe, è questa."
        ),
        "rows": [
            ("Burro bianco", "Riduci, poi monti burro freddo", "Non tiene per tutto il servizio"),
            ("Mantecare", "È solo il gesto finale", "Non include scalogno e aceto"),
            ("Gastrique", "Caramello allentato con aceto", "Non è un'emulsione di burro"),
            ("Maionese", "Emulsione fredda, più ferma", "Non si monta su una riduzione calda"),
        ],
        "faq": [
            (
                "Burro bianco e beurre blanc sono uguali?",
                "Sì. Burro bianco è il nome italiano, beurre blanc è il francese "
                "che trovi ancora scritto nei menu e nei cerca. La salsa è una: "
                "scalogno sfumato con vino bianco e aceto, riduzione, poi burro "
                "freddo montato fuori dal bollore pieno. Cambiare grafia non "
                "cambia il gesto.",
            ),
            (
                "Perché il burro bianco si rompe?",
                "Perché è un'emulsione instabile di burro in una riduzione acida, "
                "senza la tenuta di una maionese. Se lo fai bollire, il grasso si "
                "separa. Se lo lasci raffreddare al passe, il burro si riaddensa "
                "a chiazze. Lo tieni caldo e fermo, e lo monti quando il piatto "
                "esce. Non è una salsa da fare al mattino.",
            ),
            (
                "Il burro bianco è mantecare?",
                "Usa il mantecare solo alla fine. Prima c'è la riduzione di "
                "scalogno, vino bianco e aceto. Mantecare, da solo, è sbattere "
                "burro freddo in una salsa calda qualsiasi, anche un fondo di "
                "carne, senza quella base. Se chiami burro bianco ogni salsa "
                "lucidata col burro, stai dando a un gesto il nome di una ricetta.",
            ),
            (
                "Si può ribollire per rianimarlo?",
                "No. Il bollore pieno è proprio ciò che lo spezza. Se si è "
                "separato, a volte lo riprendi fuori dal fuoco, con un poco della "
                "sua riduzione ancora calda e la frusta, ma non contarci come "
                "metodo di servizio. La strada pulita è montarne poco quando il "
                "pesce è pronto, e non tenerlo in attesa.",
            ),
        ],
        "alt": [
            "Riduzione chiara di scalogno, vino bianco e aceto prima del burro",
            "Burro freddo montato nella riduzione, emulsione chiara e instabile",
            "Burro bianco appena montato su un pesce al passe, superficie lucida",
        ],
        "tags": '["burro bianco", "beurre blanc", "emulsione", "salse"]',
        "links": [
            ("montar", "mantecare, il gesto del burro"),
            ("emulsion", "che cos'è un'emulsione"),
            ("gastrique", "la gastrique e l'aceto"),
        ],
    },
    "gastrique": {
        "title": "Gastrique: caramello allentato con aceto, non l'agrodolce",
        "description": (
            "La gastrique è caramello allentato con aceto: un acido dolce, scuro, "
            "corto. L'agrodolce italiano è un parente, non lo stesso gesto, e non "
            "va usato come sinonimo."
        ),
        "term": "Gastrique",
        "lead": (
            "La gastrique è caramello allentato con aceto. Prima lo zucchero "
            "scuro, poi l'aceto che lo apre. L'agrodolce italiano è un parente, "
            "non lo stesso gesto e non un sinonimo. Condisce una salsa o un "
            "arrosto. Non è una salsa madre e non è un'emulsione. Nasce da quel "
            "gesto, non da un nome generico."
        ),
        "paras": [
            (
                "La mise en place è zucchero e aceto, niente burro, niente farina, "
                "niente tuorlo. Lo zucchero lo porti a caramello. Quando è scuro "
                "e profuma di cotto, non di bruciato amaro, lo allenti con "
                "l'aceto: il liquido freddo rispetto al caramello lo frena e lo "
                "scioglie in un succo corto. Non è lo sfumare di una padella. "
                "Sfumare scioglie il fondo di cottura attaccato al metallo. Qui "
                "non c'è un fondo da staccare. C'è un caramello da rendere "
                "versabile e acido. Se versi l'aceto troppo tardi, su uno zucchero "
                "già nero, l'amaro resta e non lo mascheri."
            ),
            (
                "In servizio la gastrique non va in tavola da sola come una ciotola "
                "da pane. La usi per svegliare una riduzione, un arrosto, una "
                "salsa che è tutta dolcezza di fondo e non ha contrasto. Ne basta "
                "il filo del giudizio, non una seconda salsa che copre il piatto. "
                "Il commensale deve sentire l'acido e il cotto dello zucchero "
                "come una linea, non come una glassa di dolce. Se la tua mano "
                "è pesante, il piatto diventa dessert salato e hai perso la "
                "carne. La tieni in un contenitore piccolo, a portata, e la "
                "dosi col cucchiaio da condimento, non col mestolo da fondo."
            ),
            (
                "L'agrodolce italiano è un parente, non lo stesso gesto. "
                "L'agrodolce, da noi in cucina, è spesso zucchero e aceto che "
                "cuociono insieme, a volte miele, a volte una conserva di "
                "verdura, cipolle, zucca, un equilibrio che vive nel piatto "
                "come condimento lungo. Non parte per forza da un caramello "
                "già fatto che poi allenti. Chiamarli sinonimi confonde chi "
                "cerca e chi cucina. Puoi dire che la gastrique ha un carattere "
                "agrodolce. Non puoi dire che ogni agrodolce è una gastrique. "
                "Il nome francese, qui, marca il gesto del caramello, non una "
                "traduzione libera."
            ),
            (
                "Il passe si appoggia alla gastrique, che ti salva i piatti che sono solo "
                "fondi ridotti, tutti sullo stesso tono. Una demi-glace "
                "profonda, un arrosto sfumato, una salsa scura: ci entri con "
                "poche gocce e il commensale trova il contrasto senza che tu "
                "abbia montato un'altra emulsione. Non sostituisce il burro "
                "bianco, che è acido e chiaro e instabile. Non sostituisce il "
                "nappante, che è una prova di corpo e non un sapore. La "
                "gastrique non lega. Se la salsa era lenta, resta lenta, solo "
                "più agra e più scura. Non usarla per coprire un difetto di "
                "corpo."
            ),
            (
                "Il margine sta nello zucchero e nell'aceto che non sprechi, e "
                "nel piatto che non devi rifare perché era piatto di sapore. "
                "Una gastrique fatta in mise en place, corta e pulita, ti dura "
                "come condimento di partita se la tieni pulita e non la "
                "contamini col mestolo di altri fondi. Non è un fondo bruno e "
                "non ne ha la profondità: non cercare lì le ossa, la tostatura, "
                "la gelatina. È un accento. Se ne fai tanta per «averla», "
                "rischi di usarla per abitudine su piatti che non la chiedono, "
                "e il commensale sente sempre la stessa nota agra. Poca, "
                "giusta, quando serve."
            ),
        ],
        "busca": (
            "La cerchi gastrique, e fai bene a non cercarla come sinonimo di "
            "agrodolce. L'agrodolce italiano è un parente: spesso zucchero e "
            "aceto insieme, un condimento, non per forza un caramello che poi "
            "allenti. La gastrique è quel gesto preciso, caramello allentato "
            "con aceto. Non è sfumare una padella, non è il burro bianco, non "
            "è una salsa madre. È un acido dolce e scuro con cui condi."
        ),
        "rows": [
            ("Gastrique", "Allenti il caramello con l'aceto", "Non è un'emulsione"),
            ("Agrodolce", "Parente italiano, altro gesto", "Non è un sinonimo"),
            ("Sfumare", "Sciogli il fondo di padella", "Non parte dallo zucchero"),
            ("Burro bianco", "Aceto in una riduzione, poi burro", "Non è caramello"),
        ],
        "faq": [
            (
                "Gastrique e agrodolce sono la stessa cosa?",
                "No. L'agrodolce italiano è un parente, non lo stesso gesto e "
                "non un sinonimo. L'agrodolce è spesso zucchero e aceto che "
                "cuociono insieme, o un condimento di verdura. La gastrique "
                "parte da un caramello già fatto e lo allenta con l'aceto. "
                "Può avere un sapore agrodolce. Non ogni agrodolce è gastrique.",
            ),
            (
                "La gastrique è una salsa madre?",
                "No. Non lega, non nappa da sola come obiettivo, non sostituisce "
                "una demi-glace o un burro bianco. È un liquido corto di "
                "caramello e aceto con cui svegli una salsa o un arrosto. Se "
                "la tua riduzione era lenta, dopo è ancora lenta, solo più "
                "agra. Il corpo si fa con un altro gesto.",
            ),
            (
                "Sfumare e fare la gastrique coincidono?",
                "No. Sfumare è sciogliere con un liquido il fondo di cottura "
                "attaccato alla padella. La gastrique non stacca un fondo: "
                "allenta un caramello con l'aceto. Tutti e due portano liquido "
                "su qualcosa di cotto e concentrato, e lì finisce la parentela. "
                "Il punto di partenza è diverso, e lo è anche il risultato.",
            ),
            (
                "Si porta in tavola da sola?",
                "Di solito no. È un condimento di cucina, un accento sulla "
                "salsa o sull'arrosto, non una ciotola da commensale. Se ne "
                "versi tanta, il piatto diventa dolce e agro e perdi la carne. "
                "La tieni piccola, in mise en place, e la dosi. Il commensale "
                "deve sentire la linea acida, non una seconda salsa.",
            ),
        ],
        "alt": [
            "Caramello scuro in pentola appena allentato con un versamento di aceto",
            "Gastrique corta e lucida in un contenitore piccolo della mise en place",
            "Poche gocce di gastrique su una salsa scura, al passe, prima di vestire la carne",
        ],
        "tags": '["gastrique", "agrodolce", "salse", "tecnica di cucina"]',
        "links": [
            ("blanc", "il burro bianco"),
            ("demi", "la demi-glace"),
            ("napar", "quando una salsa è nappante"),
        ],
    },
    "yema": {
        "title": "Legante al tuorlo: temperalo e non farlo bollire",
        "description": (
            "Il legante al tuorlo si tempera col liquido caldo e si riporta in "
            "pentola senza bollire: se bolle, il tuorlo coagula. Non è una olandese, è un legante."
        ),
        "term": "Legante al tuorlo",
        "lead": (
            "Il legante al tuorlo addensa un liquido caldo col tuorlo, non con "
            "farina o amido. Lo temperi, lo riporti in pentola, fuori dal bollore. "
            "Se bolle, il tuorlo coagula. Non è una olandese: quella è un'emulsione "
            "di tuorlo e burro. Qui il tuorlo è solo un legante."
        ),
        "paras": [
            (
                "La mise en place è il tuorlo già separato, in una ciotola, non "
                "l'uovo intero da rompere col passe addosso. Il liquido che "
                "vuoi legare — un fondo, una vellutata, una crema di servizio — "
                "è caldo e si muove appena. Ne prendi un poco, lo versi sul "
                "tuorlo sbattendo, e lo allunghi finché il tuorlo non è più un "
                "blocco freddo ma un liquido tiepido e liscio. Questo è "
                "temperare. Se salti il passaggio e butti il tuorlo freddo "
                "nella pentola, coagula a fili appena tocca il caldo, e non "
                "c'è frusta che lo riporti indietro."
            ),
            (
                "Poi lo riporti in pentola. Lo versi nel liquido che sobbolle "
                "appena, o meglio ancora in una pentola che hai tolto dal "
                "bollore, e giri. Il tuorlo lega se resta sotto la cottura che "
                "lo fa prendere come uovo strapazzato. Se bolle, coagula: vedi "
                "grumi, la salsa si spezza, il lucido diventa granuloso. Non "
                "alzare il fuoco «per farla prendere prima». La prendi con la "
                "pazienza del caldo dolce. Assaggi col cucchiaio: deve coprire "
                "un poco di più di prima, e deve restare liscia. Se senti uovo "
                "cotto a pezzi, hai passato il segno."
            ),
            (
                "Non è una olandese. L'olandese è un'emulsione: tuorlo e burro "
                "fuso, costruita come una salsa a sé, che teme il caldo per "
                "un altro motivo e non si riporta in un fondo che sobbolle. "
                "Il legante al tuorlo entra in un liquido già esistente per "
                "dargli corpo, e di burro montato non ha bisogno per chiamarsi "
                "così. Non è neanche il beurre manié, che usa farina cruda, e "
                "non è la sospensione di amido, che spegne la luce. Il tuorlo "
                "lega e tiene un certo velluto, finché non lo maltratti. "
                "Confonderlo con l'olandese ti fa cercare burro chiarificato "
                "dove ti serviva solo un legante."
            ),
            (
                "Il passe vuole questa legatura tardi, come il mantecare, "
                "perché non sopporta l'attesa sul fuoco. Una vellutata legata "
                "al tuorlo che resta a bollire in un angolo è già persa, anche "
                "se poco prima era perfetta. Organizzi la mise en place dei "
                "tuorli, e il gesto lo fai quando la comanda è vera. Il "
                "commensale non perdona i grumi: legge uovo cotto male, non "
                "«legante». Se la salsa arriva liscia e un poco più morbida "
                "di una riduzione spinta, hai fatto il tuo. Se arriva a "
                "fiocchi, non la salvi col nome tecnico."
            ),
            (
                "Il margine qui è anche sanitario e di brigata, non solo di "
                "piatto. I tuorli aperti aspettano poco, e una pentola che "
                "coagula è da buttare o da filtrare con un risultato stanco. "
                "Meglio legare la quantità che esce, non tutta la gastronomia "
                "del giorno «già che ci sei». Il commensale della crema o "
                "della vellutata cerca seta. Tu gliela dai col tuorlo temperato "
                "e col fuoco basso. Se ti serve una tenuta lunga, da tenere "
                "calda senza sorveglianza, questo non è il legante: scegli un "
                "gesto che sopporta il passe, e lascia il tuorlo ai piatti "
                "che escono subito."
            ),
        ],
        "busca": (
            "Lo cerchi legante al tuorlo, non «olandese» e non «emulsione». "
            "Temperi il tuorlo con un poco del liquido caldo e lo riporti in "
            "pentola, fuori dal bollore: se bolle, il tuorlo coagula. L'olandese "
            "è un'altra salsa, tuorlo e burro montati a sé. Qui il tuorlo entra "
            "in un liquido già fatto per dargli corpo. Se cerchi farina cruda, "
            "quello è il beurre manié, non questo gesto."
        ),
        "rows": [
            ("Legante al tuorlo", "Temperi e riporti in pentola", "Se bolle, coagula"),
            ("Olandese", "Emulsione di tuorlo e burro", "Non è un legante da fondo"),
            ("Beurre manié", "Farina cruda, non tuorlo", "Non velluta come l'uovo"),
            ("Amido", "Addensa e spegne la luce", "Non teme il bollore come il tuorlo"),
        ],
        "faq": [
            (
                "Come si tempera il tuorlo?",
                "Allunghi il tuorlo, in ciotola, con un poco del liquido caldo "
                "della pentola, sbattendo, finché non è tiepido e liscio. Poi "
                "lo riporti nella pentola, fuori dal bollore pieno, e giri. "
                "Se butti il tuorlo freddo diretto nel caldo, coagula a fili "
                "subito. Temperare è il passaggio che ti evita quei fili.",
            ),
            (
                "Cosa succede se la salsa bolle?",
                "Il tuorlo coagula. La salsa si straccia, fa grumi, perde il "
                "liscio e sa di uovo cotto a pezzi. Non si rianima alzando "
                "ancora il fuoco né sbattendo più forte: la cottura del tuorlo "
                "non torna indietro. Tieni il liquido che si muove appena, "
                "leghi, e mandi. Se doveva aspettare a bollore, hai scelto il "
                "legante sbagliato.",
            ),
            (
                "Il legante al tuorlo è una olandese?",
                "No. L'olandese è un'emulsione costruita con tuorlo e burro, "
                "una salsa a sé. Il legante al tuorlo entra in un liquido che "
                "esiste già, un fondo o una vellutata, per dargli corpo. Non "
                "ti serve il burro montato per definirlo. Se cerchi l'olandese "
                "e fai solo questo, ti manca tutta la salsa.",
            ),
            (
                "Si può fare con l'uovo intero?",
                "Il gesto di cui parliamo è il tuorlo. L'albume coagula in un "
                "altro modo e non ti dà la stessa seta. Se usi l'uovo intero "
                "sperando nello stesso risultato, cambi legante e cambi "
                "bocca. Tieni i tuorli separati in mise en place e tempera "
                "quelli. L'albume, in questa legatura, non ti aiuta.",
            ),
        ],
        "alt": [
            "Tuorlo in ciotola allungato con liquido caldo, il gesto di temperare",
            "Tuorlo temperato versato in una pentola fuori dal bollore, frusta in mano",
            "Salsa liscia legata al tuorlo, senza grumi, controllata col cucchiaio al passe",
        ],
        "tags": '["legante al tuorlo", "tuorlo", "salse", "legatura"]',
        "links": [
            ("emulsion", "l'emulsione, che non è questo legante"),
            ("montar", "mantecare col burro freddo"),
            ("blanc", "il burro bianco"),
        ],
    },
    "glace": {
        "title": "Glace de viande: il fondo ridotto finché nappa e gelifica",
        "description": (
            "La glace de viande è fondo bruno ridotto finché nappa e, a freddo, "
            "gelifica. Va oltre la demi-glace. Il fondo bruno ha un articolo suo, qui non lo ricuoci."
        ),
        "term": "Glace de viande",
        "lead": (
            "La glace de viande è un fondo bruno ridotto finché nappa e, quando "
            "si raffredda, gelifica. Va oltre la demi-glace: non ti fermi al "
            "velo, spingi finché il freddo la tiene come gelatina. Non è il "
            "fondo di partenza. È l'estratto, il punto più corto. Lo usi poco, "
            "per dare profondità."
        ),
        "paras": [
            (
                "La mise en place di una glace non è la cottura delle ossa. "
                "Quella profondità — tostatura, lunghezza, corpo del fondo "
                "bruno — sta nell'articolo dedicato al fondo bruno, e lì va "
                "lasciata. Qui parti da un fondo bruno già fatto e lo riduci. "
                "Sfumare un arrosto e raccogliere quel succo è un parente "
                "stretto, sullo stesso camino: liquido di carne che diventa "
                "corto. Non rifare in questa scheda la pentola delle ossa. "
                "Distingui solo fino a dove spingi la riduzione, perché è lì "
                "che il fondo diventa glace e smette di essere fondo."
            ),
            (
                "La riconosci in due momenti, non in uno. Calda, nappa: copre "
                "il dorso del cucchiaio con un velo scuro, lucido, che non "
                "scorre come il fondo da cui sei partito. Fredda, gelifica. "
                "Se la metti al freddo e resta liquida, non sei arrivato: ti "
                "manca riduzione. Se gelifica e, quando la scaldi, torna "
                "morbida e di nuovo nappante, sei nella glace. La demi-glace "
                "si ferma prima. Nappa, condisce, veste, e non ti chiede di "
                "diventare una gelatina. Superare quel punto è la definizione, "
                "non un optional da chef annoiato."
            ),
            (
                "Non chiamarla demi-glace per abbreviare, e non chiamarla "
                "fondo bruno perché è nata da lì. Il fondo bruno è la materia "
                "lunga, non salata come un brodo di tazza, pensata per essere "
                "lavorata. La demi-glace è salsa spagnola e fondo bruno ridotti "
                "finché nappano. La glace è oltre: meno volume, più concentrazione, "
                "il freddo che la tiene in piedi. Se le usi come sinonimi, in "
                "carta prometti un velo e in pentola hai un estratto, o il "
                "contrario, e il piatto cambia peso. Il commensale non legge "
                "i nomi. Sente se la carne è lucidata o se è coperta da un "
                "fondo ancora lungo."
            ),
            (
                "Il passe usa la glace come concentrato, non come sugo "
                "da mestolate. Ne sciogli poca in un succo di arrosto, in una "
                "sfumatura di padella, in una salsa che chiede profondità senza "
                "altro fuoco. Se la tratti come un fondo e la allunghi "
                "senza giudizio, torni indietro e perdi il lavoro di riduzione. "
                "Se la mandi pura e fredda, è una gelatina, non una salsa. La "
                "scaldi quanto basta a velare. Il commensale vede brillantezza "
                "e sapore corto, da carne, non un lago. La tua mano deve essere "
                "quella di chi condisce, non quella di chi riempie."
            ),
            (
                "Il margine di una glace è il volume che sparisce. Ridurre "
                "oltre la demi-glace vuol dire accettare poca resa e tanta "
                "presenza nel piatto. Non ha senso farla per annegare le "
                "comande: a quel punto ti serviva un fondo, e il fondo bruno "
                "ha già la sua scheda. Ha senso farla quando vuoi profondità "
                "in un cucchiaio, da tenere in mise en place e sciogliere "
                "all'ultimo. Se la riduci fino all'amaro, hai passato anche "
                "la glace: il dolce di carne diventa bruciato e il commensale "
                "lo sente prima del nome. Ti fermi quando nappa da calda e "
                "gelifica da fredda. Non un passo dopo per principio."
            ),
        ],
        "busca": (
            "La cerchi glace de viande, a volte solo glace, e non come "
            "sinonimo di demi-glace né di fondo bruno. La demi-glace nappa e "
            "si ferma. La glace de viande va oltre: nappa da calda e a freddo "
            "gelifica. Il fondo bruno è la base lunga, e la sua cottura sta "
            "altrove. Se cerchi demiglace o demi-glace trovi il grado "
            "precedente, non questo estratto."
        ),
        "rows": [
            ("Glace de viande", "Riduci finché nappa e gelifica", "Non è il fondo di partenza"),
            ("Demi-glace", "Nappa e si ferma prima", "A freddo non è la stessa gelatina"),
            ("Fondo bruno", "La base lunga, non la glace", "La sua cottura sta altrove"),
            ("Sfumatura d'arrosto", "Parente corto di padella", "Non sostituisce la riduzione del fondo"),
        ],
        "faq": [
            (
                "La glace de viande è una demi-glace?",
                "No. La demi-glace è salsa spagnola e fondo bruno ridotti "
                "finché nappano. La glace de viande va oltre quel punto: "
                "continui finché, a freddo, gelifica. Da calda nappa anche "
                "lei, ed è per questo che si confondono. Il freddo ti dice "
                "la verità. Se resta liquida, non è ancora glace.",
            ),
            (
                "Che differenza c'è col fondo bruno?",
                "Il fondo bruno è la materia lunga: ossa, tostatura, cottura. "
                "Quella profondità ha un articolo suo, e qui non la rifai. "
                "La glace de viande è quel fondo già fatto, ridotto finché "
                "nappa e a freddo gelifica. Il fondo si lavora. La glace si "
                "usa, poca, per dare concentrazione al piatto.",
            ),
            (
                "Perché a freddo deve gelificare?",
                "Perché è il segno che la riduzione ha concentrato abbastanza "
                "il corpo del fondo. Calda, la prova del cucchiaio ti dice "
                "che nappa. Fredda, la gelatina ti dice che sei oltre la "
                "demi-glace. Se al freddo resta sciolta, ti manca fuoco e "
                "tempo di riduzione, non un altro nome. Non è una salsa da "
                "servire gelata: la riscaldi per velare.",
            ),
            (
                "Si manda in tavola pura?",
                "Di solito no. È un concentrato da sciogliere in un succo, in "
                "una sfumatura, in una salsa che chiede profondità. Pura e "
                "fredda è una gelatina. Pura e calda, a mestolate, annega il "
                "piatto e spreca la riduzione. Il commensale deve trovare "
                "un velo, non un fondo ributtato nel piatto col nome di glace.",
            ),
        ],
        "alt": [
            "Glace de viande scura che copre il dorso del cucchiaio, ancora calda",
            "Glace raffreddata che gelifica nel contenitore, segno che la riduzione è arrivata",
            "Un velo di glace sciolta su una carne al passe, senza allagare il piatto",
        ],
        "tags": '["glace de viande", "fondi", "salse", "fondo bruno"]',
        "links": [
            ("demi", "la demi-glace, il grado prima"),
            ("fumet", "il fumetto, un altro fondo"),
            ("napar", "la prova del cucchiaio"),
            ("https://aichef.pro/it/blog/fondo-bruno", "il fondo bruno"),
        ],
    },
    "fumet": {
        "title": "Fumetto: lische e aromi, senza la tostatura del fondo bruno",
        "description": (
            "Il fumetto è un fondo di lische e aromi, non tostati come il fondo "
            "bruno. Se cuoce troppo, esce amaro. Non è una zuppa da portare al "
            "commensale: è una base."
        ),
        "term": "Fumetto",
        "lead": (
            "Il fumetto è il fondo del pesce: lische e aromi, non ossa tostate "
            "come nel fondo bruno. Se insisti troppo a lungo esce amaro. Non è "
            "una zuppa da portare in tavola. È una base per salse. In francese "
            "lo cerchi anche come fumet. Lo riduci, non lo servi."
        ),
        "paras": [
            (
                "La mise en place sono lische pulite, senza branchie e senza "
                "il sangue che intorbida, e aromi che non devono dominare il "
                "pesce. Non le tosti come tosti le ossa del fondo bruno. "
                "Quella tostatura è un altro mondo: colore, amaro dolce di "
                "carne, cottura lunga. Il fumetto, se lo bruni, perde il "
                "chiaro e prende un cotto che non gli appartiene. La "
                "profondità del fondo bruno — come si tosta, come si tiene, "
                "come si usa sulla carne — sta nell'articolo del fondo bruno. "
                "Qui non la ripeti. Qui distingui: lische e aromi, pentola "
                "docile, niente crosta scura di partenza."
            ),
            (
                "Se lo fai cuocere troppo, escono note amare. Non è un fondo "
                "che migliora solo perché resta sul fuoco. Il pesce dà in "
                "fretta quello che ha, e poi la lisca, la pelle, l'aroma "
                "spinto diventano amari e il liquido si stanca. Lo schiumi, "
                "lo tieni a un sobbollire quieto, lo coli presto rispetto "
                "all'idea di «fondo che va avanti da solo». Non è una zuppa "
                "da portare al commensale. Un brodo di pesce salato, finito, "
                "bevuto in tazza, è un altro piatto. Il fumetto non lo sali "
                "come una zuppa: lo ridurrai, lo monterai, lo userai, e il "
                "sale si concentrerebbe."
            ),
            (
                "Non è la glace de viande e non è un fondo bruno fatto col "
                "pesce per sbaglio. La glace è carne ridotta finché gelifica. "
                "Il fondo bruno è tostato. Il fumetto resta la base chiara "
                "del pesce. Da lui puoi ridurre, puoi legare, puoi montare "
                "un burro bianco se la riduzione di scalogno e aceto ci sta "
                "bene sopra, puoi cercare un punto nappante. Non gli chiedere "
                "la gelatina scura di un fondo di vitello. Se lo tratti come "
                "se dovesse diventare glace di carne, lo cuoci troppo e lo "
                "fai amaro, che è l'errore tipico di chi ha una sola pentola "
                "mentale per tutti i fondi."
            ),
            (
                "Il passe vuole il fumetto già come salsa o come "
                "velo, quasi mai come il liquido del mattino. Lo riduci, lo "
                "mantechi, lo nappi sul pesce. Il commensale mangia quella "
                "salsa, non una ciotola di fumetto col nome scritto sopra. "
                "Se gli mandi il fondo lungo, legge brodo, e aveva ordinato "
                "un piatto. La mise en place giusta è fumetto colato, pulito, "
                "pronto a diventare corto, più il burro freddo se la carta "
                "chiede luce. Non tieni le lische in pentola durante il "
                "servizio sperando che «finiscano di dare». A quel punto hanno "
                "già dato, o hanno già amareggiato."
            ),
            (
                "Il margine del fumetto è il pesce che non butti due volte. "
                "Le lische sono ciò che resta dopo aver messo via i filetti: "
                "farne una base è rispetto del prodotto, a patto di non "
                "rovinarla con una cottura da fondo bruno. Se esce amaro, "
                "hai perso le lische e il tempo, e il commensale non perdona "
                "l'amaro sul pesce. Meglio un fumetto corto e pulito, usato "
                "subito in salsa, che un liquido tenuto tutto il giorno "
                "perché «i fondi si fanno così». I fondi di carne si fanno "
                "così. Questo no. La scheda del fondo bruno tiene quella "
                "profondità. Tu, qui, fermati prima dell'amaro."
            ),
        ],
        "busca": (
            "In Italia lo cerchi fumetto, ed è la parola del pesce. La grafia "
            "fumet è quella francese, lo stesso fondo: lische e aromi, non tostati "
            "come il fondo bruno. Non cercarlo come zuppa e non cercarlo come "
            "glace de viande. Se cuoce troppo diventa amaro. Se cerchi la "
            "tostatura e la lunghezza delle ossa di carne, quello è il fondo "
            "bruno, ed è un altro articolo. Il fumetto è la base chiara."
        ),
        "rows": [
            ("Fumetto", "Lische e aromi, non tostati", "Se cuoce troppo, amaro"),
            ("Fondo bruno", "Ossa di carne tostate", "Non è la base del pesce"),
            ("Zuppa di pesce", "Piatto, spesso salato", "Il fumetto non si porta in tavola"),
            ("Glace de viande", "Carne ridotta che gelifica", "Non si fa con le lische"),
        ],
        "faq": [
            (
                "Fumetto e fumet sono la stessa cosa?",
                "Sì. Fumetto è il nome che usi in Italia, fumet è la grafia "
                "francese che trovi nei testi e nei cerca. In tutti e due i "
                "casi parli di un fondo di lische e aromi, non tostato come "
                "il fondo bruno. Non è una zuppa. È una base da ridurre, "
                "legare o montare per il pesce.",
            ),
            (
                "Il fumetto è un fondo bruno di pesce?",
                "No. Il fondo bruno tosta le ossa e cuoce a lungo: quella "
                "profondità ha un articolo suo e non si copia sulle lische. "
                "Il fumetto parte da lische e aromi senza quella crosta. Se "
                "lo bruni e lo tieni sul fuoco come un fondo di carne, perde "
                "il chiaro e prende note amare. Sono due fondi diversi.",
            ),
            (
                "Perché il fumetto diventa amaro?",
                "Perché il pesce dà in fretta e poi la cottura lunga tira "
                "fuori amaro da lisca, pelle e aromi spinti. Non è un fondo "
                "che migliora solo restando in pentola. Lo tieni a sobbollire "
                "quieto, lo schiumi, lo coli senza insistere. Se cercavi la "
                "lunghezza del fondo bruno, sei nel capitolo sbagliato.",
            ),
            (
                "Si può servire il fumetto come zuppa?",
                "No, non è una zuppa da portare al commensale. Non lo sali "
                "come un brodo di tazza, perché poi lo riduci e il sale si "
                "concentra. Un brodo di pesce finito, condito, servito, è "
                "un altro piatto. Il fumetto resta in cucina e diventa salsa, "
                "velo, base di un burro bianco. In tavola arriva trasformato.",
            ),
        ],
        "alt": [
            "Lische di pesce e aromi in pentola, senza tostatura, per un fumetto chiaro",
            "Fumetto colato, limpido, in un contenitore della mise en place",
            "Salsa di pesce nata dal fumetto, lucida sul piatto al passe",
        ],
        "tags": '["fumetto", "fumet", "pesce", "fondi"]',
        "links": [
            ("glace", "la glace de viande"),
            ("blanc", "il burro bianco sul pesce"),
            ("papilla", "legare con l'amido"),
            ("https://aichef.pro/it/blog/fondo-bruno", "il fondo bruno"),
        ],
    },
    "papilla": {
        "title": "Sospensione di amido: scioglila a freddo, poi nel liquido",
        "description": (
            "La sospensione di amido è amido sciolto in liquido freddo e versato "
            "nel liquido che sobbolle. Lega in fretta e spegne la lucentezza "
            "della salsa. Non è un roux."
        ),
        "term": "Sospensione di amido",
        "lead": (
            "La sospensione di amido è amido sciolto in liquido freddo, poi "
            "versato nel liquido che sobbolle. Se lo butti secco nel caldo, fa "
            "grumi. Lega in fretta e spegne la lucentezza. Non è un roux e non "
            "è burro montato. La salsa diventa opaca, e lo sai prima."
        ),
        "paras": [
            (
                "La mise en place è una ciotolina: amido e liquido freddo, "
                "sciolti prima che ti servano, non la polvere buttata al volo "
                "sopra il bollore. Acqua fredda, o un fondo freddo, basta a "
                "disperdere l'amido. Giri finché non vedi più grumi sul fondo "
                "della ciotola. Quella è la sospensione. La tieni pronta "
                "accanto alla pentola. Se la prepari e la abbandoni, l'amido "
                "si sedimenta: la rimesti prima di versarla, altrimenti versi "
                "acqua sopra e polvere sotto, e il gesto non parte. Rimesta, "
                "e solo allora è pronta per il liquido che sobbolle."
            ),
            (
                "Poi la versi nel liquido che sobbolle, girando. Il caldo è "
                "ciò che fa prendere l'amido: a freddo la sospensione è solo "
                "opaca e lenta, non è ancora una legatura. Nel sobbollire il "
                "corpo arriva, e arriva in fretta, ed è per questo che al "
                "passe ti tenta. Appena il cucchiaio si veste, ti fermi. Se "
                "continui a versare perché «un altro giro non fa male», la "
                "salsa diventa colla. Il commensale la sente attaccata al "
                "palato, non morbida. Questo legante non perdona la mano "
                "pesante, proprio perché lavora subito."
            ),
            (
                "Spegne la lucentezza. Una riduzione che avevi lucidato col "
                "burro, o una demi-glace che rifletteva, dopo l'amido si "
                "opacizza. Non è un difetto nascosto: è l'effetto del gesto. "
                "Lo accetti quando ti serve corpo subito e il piatto sopporta "
                "una salsa meno brillante. Non lo accetti quando la carta "
                "promette una salsa lucida e tu la spegni all'ultimo per "
                "pigrizia. Il roux, la farina cotta nel grasso, costruisce "
                "un corpo diverso e un sapore di cotto. Il beurre manié porta "
                "burro insieme alla farina. Qui c'è solo amido. Nessuna di "
                "queste strade è «la buona» in assoluto. Sono tre risposte a "
                "tre problemi."
            ),
            (
                "Il passe usa l'amido come rete quando non hai roux pronto e "
                "non vuoi cambiare il sapore con una tostatura. Un salto di "
                "verdura troppo brodoso, un fondo che deve tenere fino al "
                "piatto senza un'altra riduzione: sciogli, versi, fermi. Il "
                "commensale non vede l'amido. Vede se la salsa sta sul pezzo "
                "o se corre nel bordo, e vede se il piatto è opaco. Tu "
                "decidi prima quale delle due cose il piatto può perdere. "
                "Se può perdere luce e non può perdere corpo, questa è la "
                "strada. Se la luce è il piatto, non toccare l'amido: monta "
                "burro o riduci."
            ),
            (
                "Il margine ama la velocità e paga in aspetto. Non butti una "
                "cottura, non apri un roux, non aspetti una riduzione lunga. "
                "In cambio il piatto perde il riflesso che una salsa di "
                "fondo, spinta fino al nappante, avrebbe tenuto. Usala come "
                "scelta, non come tic. La mise en place della ciotolina "
                "fredda ti evita i grumi, che sono lo spreco vero: una salsa "
                "grumosa si filtra male e spesso si rifà. Il commensale di "
                "un piatto lucido non va consolato con la frase «è legato». "
                "O la luce c'era, o hai scelto l'amido a ragion veduta."
            ),
        ],
        "busca": (
            "La cerchi come sospensione di amido, o semplicemente amido "
            "sciolto a freddo. Non è un roux e non è il beurre manié. "
            "L'amido va disperso in liquido freddo e poi versato nel liquido "
            "che sobbolle: se lo butti secco, fa grumi. Lega in fretta e "
            "spegne la lucentezza. Se cerchi luce, manteca o riduci. Se "
            "cerchi corpo subito e accetti una salsa opaca, è questo il gesto."
        ),
        "rows": [
            ("Sospensione di amido", "Sciogli a freddo, poi nel caldo", "Spegne la lucentezza"),
            ("Amido secco in pentola", "Fa grumi subito", "Non è il gesto"),
            ("Roux", "Farina cotta nel grasso", "Cambia sapore e colore"),
            ("Burro montato", "Dà luce, non questo corpo", "Non opacizza come l'amido"),
        ],
        "faq": [
            (
                "Perché l'amido si scioglie a freddo?",
                "Perché nel liquido freddo si disperde. Se lo butti secco nel "
                "liquido caldo, la parte esterna gelifica subito e chiude la "
                "polvere in grumi che la frusta non apre. Prima fai la "
                "sospensione, liscia, in una ciotola fredda. Poi la versi nel "
                "liquido che sobbolle, girando. L'ordine è il gesto.",
            ),
            (
                "Perché la salsa perde luce?",
                "Perché l'amido opacizza. Una riduzione o un burro montato "
                "riflettono; dopo questa legatura la superficie si spegne. "
                "Non è un incidente, è l'effetto del gesto. Lo scegli quando "
                "ti serve corpo subito e il piatto può perdere brillantezza. "
                "Se la luce è il punto del piatto, non usare l'amido.",
            ),
            (
                "La sospensione di amido è un roux?",
                "No. Il roux cuoce la farina in un grasso prima del liquido, "
                "e può essere bianco, biondo o bruno. Qui non c'è grasso e "
                "non c'è quella cottura: c'è amido sospeso in liquido freddo, "
                "poi il caldo della pentola. Anche il beurre manié è un'altra "
                "cosa, perché porta burro e farina crudi insieme.",
            ),
            (
                "Quando ti fermi?",
                "Appena la salsa copre il cucchiaio quanto ti serve. L'amido "
                "prende in fretta e, se insisti, diventa colla. Il commensale "
                "la sente attaccata, non morbida. Versi, giri, guardi, e "
                "smetti. Il resto della sospensione non va «già che c'è». "
                "Una salsa troppo legata non si allunga senza perdere il "
                "sapore che avevi.",
            ),
        ],
        "alt": [
            "Amido sciolto in liquido freddo in una ciotola, senza grumi, prima della pentola",
            "Sospensione di amido versata in un liquido che sobbolle, mentre la frusta gira",
            "Salsa legata con amido, opaca rispetto a una riduzione lucida tenuta accanto",
        ],
        "tags": '["amido", "legatura", "salse", "tecnica di cucina"]',
        "links": [
            ("roux", "il roux"),
            ("manie", "il beurre manié"),
            ("napar", "il punto nappante"),
        ],
    },
    "roux": {
        "title": "Roux: farina cotta nel grasso, bianco, biondo e bruno",
        "description": (
            "Il roux è farina cotta nel grasso prima del liquido, a parti uguali, "
            "a peso. Bianco, biondo o bruno. In tedesco: Mehlschwitze. Non è il beurre manié."
        ),
        "term": "Roux",
        "lead": (
            "Il roux è farina cotta nel grasso prima del liquido, a parti uguali, "
            "a peso. Bianco, biondo o bruno: cambia il gusto, dal neutro al "
            "tostato. In tedesco è la Mehlschwitze. Non è il beurre manié, crudo "
            "e di fine cottura, e non è l'amido sciolto a freddo."
        ),
        "paras": [
            (
                "La mise en place del roux è grasso e farina, a parti uguali, "
                "a peso, e una pentola che puoi girare senza abbandonarla. "
                "Fai fondere il grasso, entri con la farina, e cuoci prima di "
                "qualsiasi liquido. Quel «prima» è tutta la definizione. La "
                "farina perde il crudo, il grasso la bagna, e i grumi che "
                "temi dopo nascono se salti questa cottura o se versi il "
                "liquido senza girare. Non è una pausa facoltativa. Se versi "
                "subito, stai bagnando farina, non stai facendo un roux. Il "
                "colore lo decidi tu, restando lì, col naso e con gli occhi, "
                "non con la fretta del passe."
            ),
            (
                "Bianco, biondo, bruno sono lo stesso gesto a tre profondità "
                "di cottura. Il bianco si ferma quando la farina non sa più "
                "di crudo e il colore è ancora chiaro: è la base delle salse "
                "che non vogliono tostatura. Il biondo profuma di cotto, di "
                "noce appena accennata, e porta un colore caldo senza "
                "dominare. Il bruno va più a lungo, scuro, con un tostato "
                "netto, e sta dalla parte delle salse di carne, accanto al "
                "fondo bruno. Più lo cuoci, più il gusto cambia. Non è una "
                "gara a chi lo fa più scuro: il bruno bruciato è amaro, e "
                "l'amaro non si chiama roux, si chiama errore."
            ),
            (
                "In tedesco lo dici Mehlschwitze: farina e grasso cotti, lo "
                "stesso ponte verso la salsa. Tenerlo a mente ti evita di "
                "credere che sia un'altra ricetta solo perché cambia lingua. "
                "Non è il beurre manié. Il beurre manié è burro morbido e "
                "farina crudi, sbriciolati a fine cottura, senza questa "
                "cottura preventiva. Non è la sospensione di amido, che non "
                "vede grasso e che spegne la luce. Il roux costruisce corpo "
                "e, se è biondo o bruno, costruisce anche sapore. Lo scegli "
                "quando la salsa deve nascere da lì, non quando devi solo "
                "salvare all'ultimo un liquido già fatto."
            ),
            (
                "Il passe riceve il roux quasi sempre già diventato "
                "salsa. La besciamella, la vellutata, la spagnola: il "
                "commensale non ordina «un roux». Ordina il piatto che ci "
                "sta sopra. Per questo il roux vive dentro la mise en place, "
                "non sulla comanda già urlata. "
                "Se al servizio ti manca corpo e non hai roux, non fingere "
                "di farlo in un bollore: o usi il beurre manié, o l'amido, "
                "e sai che il risultato non sarà lo stesso. Il commensale "
                "sente il crudo della farina se hai avuto fretta. Quella "
                "fretta non si maschera col nome francese."
            ),
            (
                "Il margine del roux è la salsa madre che ti evita tante "
                "salse diverse fatte male. Un roux bianco ti apre le salse "
                "di latte. Un biondo ti apre i vellutati. Un bruno ti sta "
                "accanto al fondo bruno quando costruisci la spagnola e, "
                "più avanti, la demi-glace. Non è il posto dove raccontare "
                "tutta la cottura del fondo: quella profondità ha la sua "
                "scheda. Qui il punto è la farina cotta nel grasso, a parti "
                "uguali, a peso, prima del liquido. Se rispetti questo, il "
                "resto della salsa ha un pavimento. Se lo salti, ogni "
                "legante d'emergenza è un cerotto, e il commensale mangia "
                "il cerotto."
            ),
        ],
        "busca": (
            "Lo cerchi roux, e in tedesco Mehlschwitze: farina cotta nel "
            "grasso prima del liquido. Bianco, biondo e bruno sono cotture "
            "diverse dello stesso gesto, non tre ricette estranee. Non "
            "cercarlo come beurre manié: quello è crudo e si usa a fine "
            "cottura. Non cercarlo come amido sciolto a freddo. Se la "
            "tastiera ti propone altre grafie, il gesto resta uno: grasso, "
            "farina, cottura, poi il liquido."
        ),
        "rows": [
            ("Roux bianco", "Cotti appena, colore chiaro", "Non porta tostatura"),
            ("Roux biondo", "Cotto, profumo di noce", "Non è ancora bruno"),
            ("Roux bruno", "Tostato, per le salse di carne", "Se brucia, è amaro"),
            ("Mehlschwitze", "Lo stesso gesto in tedesco", "Non è un'altra ricetta"),
        ],
        "faq": [
            (
                "Il roux è burro e farina a crudo?",
                "No, quello è il beurre manié. Il roux cuoce la farina nel "
                "grasso prima del liquido. Burro o un altro grasso, farina, "
                "a parti uguali, a peso, e una cottura vera, girando, finché "
                "il crudo se ne va. Se non cuoci, non è roux. Se sbricioli "
                "la pasta a fine cottura, hai cambiato nome e cambiato gesto.",
            ),
            (
                "Che differenza c'è tra bianco, biondo e bruno?",
                "La cottura. Il bianco si ferma chiaro, quando la farina non "
                "sa più di crudo. Il biondo prende colore e un profumo di "
                "cotto. Il bruno va oltre, tostato, e sta con le salse di "
                "carne. Non sono tre ricette con ingredienti diversi. È lo "
                "stesso grasso e la stessa farina, tenuti sul fuoco per un "
                "tempo di giudizio diverso. Il bruno bruciato non vale: è amaro.",
            ),
            (
                "Che cos'è la Mehlschwitze?",
                "È il nome tedesco del roux. Farina cotta nel grasso prima "
                "del liquido, lo stesso gesto. Non è una salsa diversa e non "
                "è un legante d'emergenza. Se in brigata senti Mehlschwitze, "
                "pensa al roux bianco, biondo o bruno, non a una ricetta "
                "nuova da imparare da zero.",
            ),
            (
                "Posso fare il roux all'ultimo, sul bollore?",
                "No. Il roux chiede la cottura della farina nel grasso prima "
                "del liquido, e questa cosa non succede dentro un bollore già "
                "avviato. All'ultimo, se ti manca corpo, usi un beurre manié "
                "o una sospensione di amido, e sai che non è la stessa salsa. "
                "Il roux si fa prima, in mise en place, con calma.",
            ),
        ],
        "alt": [
            "Farina appena entrata nel grasso fuso, inizio di un roux ancora chiaro",
            "Tre roux a confronto, bianco, biondo e bruno, in tre pentolini della partita",
            "Roux bruno cotto nel grasso prima del liquido, profumo di tostato senza bruciato",
        ],
        "tags": '["roux", "Mehlschwitze", "salse", "legatura"]',
        "links": [
            ("manie", "il beurre manié, che resta crudo"),
            ("papilla", "la sospensione di amido"),
            ("demi", "la demi-glace"),
        ],
    },
    "emulsion": {
        "title": "Emulsione: due liquidi tenuti da tuorlo, senape o lecitina",
        "description": (
            "Un'emulsione tiene insieme due liquidi che non si mescolano, con "
            "tuorlo, senape o lecitina. Maionese, olandese e vinaigrette non "
            "hanno la stessa tenuta sul passe."
        ),
        "term": "Emulsione",
        "lead": (
            "Un'emulsione tiene due liquidi che da soli non si mescolano. "
            "Il tuorlo, la senape o la lecitina li tiene. Maionese, olandese "
            "e vinaigrette non hanno la stessa tenuta: una sta, una teme il "
            "caldo, una si separa. Non è un roux e non è amido. Sono tre "
            "tenute, non una salsa sola."
        ),
        "paras": [
            (
                "La mise en place di un'emulsione è il contenitore freddo o "
                "caldo giusto, e l'ingrediente che tiene. Il tuorlo tiene "
                "molto, ed è il cuore della maionese e dell'olandese. La "
                "senape tiene meno, e però aiuta una vinaigrette a restare "
                "insieme abbastanza da condire. La lecitina è il nome di "
                "ciò che, nel tuorlo e in altri ingredienti, fa questo "
                "lavoro: non è una salsa, è la ragione per cui due liquidi "
                "nemici accettano di stare nello stesso cucchiaio. Se non "
                "c'è niente che tenga, olio e aceto, o burro e acqua, si "
                "lasciano. Sempre. L'emulsione non è un desiderio, è un "
                "appoggio."
            ),
            (
                "La maionese è l'emulsione fredda di tuorlo e olio. Se la "
                "costruisci con calma e la tieni al fresco della partita, "
                "ha una tenuta che ti porta attraverso il servizio. L'olandese "
                "è calda: tuorlo e burro, e teme sia il freddo che la "
                "dimentichi sia il caldo che la fai bollire. Al passe vive "
                "poco, e la guardi. La vinaigrette è la più fragile delle "
                "tre: senape, aceto, olio, la sbatti, condisci, e se aspetta "
                "si separa. La rimonti. Non è un fallimento morale, è la sua "
                "tenuta. Trattarle come se fossero la stessa salsa col "
                "cambia-nome è il modo in cui si manda in sala un condimento "
                "rotto."
            ),
            (
                "Non confondere l'emulsione col legante al tuorlo. Il legante "
                "al tuorlo entra in un liquido già in pentola, si tempera, "
                "si riporta dentro, e se bolle coagula: sta addensando un "
                "fondo, non sta tenendo olio in tuorlo. L'olandese usa il "
                "tuorlo, sì, ma come emulsione di burro, ed è una salsa a "
                "sé. Il burro bianco è un'emulsione instabile anche lui, "
                "senza tuorlo obbligatorio: burro montato su una riduzione. "
                "Il roux non è un'emulsione. L'amido non è un'emulsione. "
                "Se chiami emulsione ogni salsa che luccica, la parola non "
                "ti serve più a decidere nulla."
            ),
            (
                "Il passe separa le tre tenute in tre organizzazioni. "
                "La maionese può aspettare, al freddo, in mise en place, e "
                "la controlli lo stesso perché un olio che si separa non si "
                "manda. L'olandese la finisci quando il piatto esce, come "
                "finisci un mantecare. La vinaigrette la sbatti di nuovo "
                "all'ultimo, e non ti vergogni: è il gesto. Il commensale "
                "vede una salsa intera oppure un piatto con l'olio che "
                "corre da una parte e l'aceto dall'altra. Non conosce la "
                "lecitina. Conosce il condimento rotto, e lo legge come "
                "fretta."
            ),
            (
                "Il margine di un'emulsione rotta è il rifacimento. Un tuorlo "
                "perso, un olio versato, una olandese che hai tenuto troppo "
                "e che non torna, sono prodotto e tempo. Per questo non "
                "emulsioni «per tutta la sera» ciò che non tiene tutta la "
                "sera. La maionese, sì, se la tieni bene. L'olandese e il "
                "burro bianco, no. La vinaigrette, la rifai in un secondo "
                "con la frusta, e il margine è salvo proprio perché non "
                "fingi che sia eterna. Il commensale non paga la tua "
                "categoria: paga un condimento che sta insieme nel piatto. "
                "Scegli l'emulsione che il servizio può tenere."
            ),
        ],
        "busca": (
            "La cerchi emulsione: due liquidi che non si mescolano, tenuti "
            "da tuorlo, senape o lecitina. Maionese, olandese e vinaigrette "
            "non hanno la stessa tenuta, anche se la parola è una. Non "
            "cercarla come roux e non cercarla come legante al tuorlo: il "
            "legante coagula se bolle, l'emulsione è un'altra costruzione. "
            "Il burro bianco è un'emulsione instabile. La maionese, se la "
            "tratti bene, tiene più a lungo."
        ),
        "rows": [
            ("Maionese", "Fredda, tuorlo e olio, tiene", "Non è una salsa calda"),
            ("Olandese", "Calda, tuorlo e burro, fragile", "Non è il legante da pentola"),
            ("Vinaigrette", "Si separa, la rimonti", "Non ha la tenuta della maionese"),
            ("Burro bianco", "Emulsione instabile, senza tuorlo", "Non è una maionese calda"),
        ],
        "faq": [
            (
                "Che cos'è un'emulsione, in cucina?",
                "È il modo in cui tieni insieme due liquidi che da soli si "
                "lasciano, per esempio olio e aceto, o burro e un liquido "
                "acqueo. A tenerli ci pensano il tuorlo, la senape o la "
                "lecitina. Senza un appoggio, i due liquidi si separano. "
                "Non è un roux e non è amido: non stai cuocendo farina, stai "
                "tenendo delle gocce in sospensione.",
            ),
            (
                "Maionese, olandese e vinaigrette tengono uguale?",
                "No. La maionese, fredda, di tuorlo e olio, tiene per il "
                "servizio se la conservi bene. L'olandese, calda, di tuorlo "
                "e burro, teme l'attesa e il bollore. La vinaigrette, aiutata "
                "dalla senape, si separa e la rimonti all'ultimo. Stessa "
                "famiglia, tre tenute. Trattarle uguali è il modo di mandare "
                "in sala la salsa già rotta.",
            ),
            (
                "L'emulsione è il legante al tuorlo?",
                "No. Il legante al tuorlo si tempera e si riporta in un "
                "liquido caldo: se bolle, coagula, e sta addensando un fondo. "
                "L'emulsione tiene due liquidi che non si mescolano, come "
                "nell'olandese o nella maionese. L'olandese usa il tuorlo, "
                "ma non è quel legante. Sono due gesti che condividono un "
                "ingrediente e nient'altro.",
            ),
            (
                "Perché il burro bianco si chiama emulsione?",
                "Perché il burro freddo, montato sulla riduzione, sta "
                "sospeso in quel liquido invece di galleggiare a chiazze. "
                "È instabile: niente tenuta da maionese, niente tuorlo "
                "obbligatorio. Se bolle, si rompe. Lo chiami emulsione per "
                "capire come trattarlo al passe, non per farlo diventare "
                "un'altra salsa fredda.",
            ),
        ],
        "alt": [
            "Tuorlo e olio che si tengono insieme in una maionese liscia, emulsione fredda",
            "Olandese calda appena montata, emulsione fragile accanto alla frusta",
            "Vinaigrette separata in un contenitore, olio e aceto in due fasi prima di rimontarla",
        ],
        "tags": '["emulsione", "maionese", "salse", "tecnica di cucina"]',
        "links": [
            ("yema", "il legante al tuorlo"),
            ("blanc", "il burro bianco"),
            ("montar", "mantecare una salsa calda"),
        ],
    },
    "demi": {
        "title": "Demi-glace: salsa spagnola e fondo bruno finché nappano",
        "description": (
            "La demi-glace è salsa spagnola e fondo bruno ridotti finché nappano. "
            "La trovi scritta demi-glace, demi glace o demiglace. Non è la glace "
            "de viande: si ferma prima."
        ),
        "term": "Demi-glace",
        "lead": (
            "La demi-glace è salsa spagnola e fondo bruno ridotti finché "
            "nappano. Non è la glace de viande, che a freddo gelifica. Le "
            "grafie sono demi-glace, demi glace e demiglace: la stessa salsa. "
            "È il velo di servizio, non l'estratto. Ti fermi quando il "
            "cucchiaio si veste."
        ),
        "paras": [
            (
                "La mise en place presuppone due cose già fatte: la salsa "
                "spagnola e il fondo bruno. Non è questa la scheda dove "
                "impari a tostare le ossa o a costruire tutta la spagnola "
                "dal roux bruno. Quelle profondità stanno altrove, e il "
                "fondo bruno ha il suo articolo. Qui i due liquidi si "
                "incontrano e si riducono. Sfumare una padella di carne e "
                "bagnarla con questa salsa è un uso, non la definizione. "
                "La definizione è la riduzione congiunta finché il cucchiaio "
                "si veste. Se parti solo dal fondo, senza la spagnola, "
                "stai facendo un fondo ridotto, e gli "
                "dai un nome che non gli tocca."
            ),
            (
                "È pronta quando nappa. Non prima, perché sarebbe ancora "
                "lunga, un fondo vestito a festa. Non dopo, fino a diventare "
                "glace: quello è un altro grado, e a freddo te lo dice "
                "perché gelifica. La demi-glace, fredda, è sciropposa e "
                "ferma, ma non è la gelatina stretta della glace. Calda, "
                "vela la carne senza diventare un estratto da dosare a "
                "gocce. Il commensale la sente come sugo profondo, continuo, "
                "non come un brodo e non come una caramella di carne. Il "
                "tuo occhio sul dorso del cucchiaio è l'unico strumento "
                "che ti serve per chiudere."
            ),
            (
                "Le grafie non fanno tre ricette. Demi-glace, con il "
                "trattino, è la scrittura francese più comune. Demi glace, "
                "staccata, è quella che esce dalla tastiera quando non "
                "cerchi il trattino. Demiglace, tutto attaccato, è l'altra "
                "ricerca. In pentola è la stessa cosa: spagnola e fondo "
                "bruno, ridotti, nappanti. Non è la glace de viande. Se "
                "un cerca ti porta alla glace e tu volevi il velo da "
                "servizio, torna indietro di una riduzione. Se ti porta "
                "al fondo bruno, sei nella materia prima, prima della "
                "salsa. I nomi vicini sono una famiglia, non sinonimi."
            ),
            (
                "Il passe manda la demi-glace come salsa che veste l'arrosto, "
                "il brasato, la carne che ha già un succo e chiede "
                "continuità. La scaldi senza strapazzarla, la lucidi se "
                "serve con un mantecare finale — burro freddo, fuori dal "
                "bollore — e la mandi quando nappa. Non la tieni a bollore "
                "violento per tutto il servizio: si concentra ancora e, senza "
                "che tu l'abbia deciso, cammina verso la glace, e il piatto "
                "cambia. Il commensale non distingue il trattino nella "
                "grafia. Distingue un sugo che copre da un fondo che allaga "
                "e da un estratto che brucia di troppo ridotto."
            ),
            (
                "Il margine sta nel non ridurre due volte per errore. La "
                "demi-glace chiede il fondo e la spagnola, cioè il lavoro "
                "lungo di cucina. Se al passe la spingi fino a glace senza "
                "volerlo, hai poca salsa e un altro prodotto, e le comande "
                "che contavano sul velo restano scoperte. Se la mandi "
                "lunga, hai sprecato il nome e il commensale mangia un "
                "quasi-fondo. Tieni in mise en place la demi già nappante, "
                "e al servizio scaldala e, se vuoi luce, mantecala. Il "
                "fondo bruno, con la sua cottura, non va rifatto in questa "
                "pagina. Qui chiudi il grado giusto e lo difendi."
            ),
        ],
        "busca": (
            "Le grafie che la gente scrive sono demi-glace, demi glace e "
            "demiglace. Sono la stessa salsa: salsa spagnola e fondo bruno "
            "ridotti finché nappano. Non cercarla come glace de viande: la "
            "glace va oltre e a freddo gelifica. Non cercarla come solo "
            "fondo bruno: il fondo è la base, prima della riduzione con la "
            "spagnola. Se il cerca stacca o attacca le parole, il gesto in "
            "pentola non cambia."
        ),
        "rows": [
            ("Demi-glace", "Spagnola e fondo bruno, finché nappa", "Non è la glace"),
            ("Demi glace", "Stessa salsa, grafia staccata", "Non è un'altra ricetta"),
            ("Demiglace", "Stessa salsa, tutto attaccato", "Non cambia il gesto"),
            ("Glace de viande", "Oltre, e a freddo gelifica", "Non è il velo di servizio"),
        ],
        "faq": [
            (
                "Demi-glace, demi glace e demiglace cambiano la salsa?",
                "No. Sono tre grafie della stessa salsa. Demi-glace porta "
                "il trattino, demi glace lo perde, demiglace attacca le "
                "parole. In pentola è sempre salsa spagnola e fondo bruno "
                "ridotti finché nappano. Non lasciare che la tastiera ti "
                "convinca di avere tre preparazioni. Il cucchiaio è uno.",
            ),
            (
                "La demi-glace è la glace de viande?",
                "No. La demi-glace si ferma quando nappa: vela la carne, "
                "resta una salsa di servizio. La glace de viande continua "
                "oltre, finché a freddo gelifica, e si usa come concentrato, "
                "poca. Se le chiami uguali, o annega il piatto o gli togli "
                "il velo. Il freddo ti aiuta a vedere dove sei arrivato.",
            ),
            (
                "Basta il fondo bruno per chiamarla demi-glace?",
                "No. Ci vogliono salsa spagnola e fondo bruno, ridotti "
                "insieme finché nappano. Un fondo bruno ridotto da solo è "
                "un fondo ridotto, e la sua cottura lunga sta nell'articolo "
                "del fondo, non qui. Se manca la spagnola, manca una parte "
                "del nome. Non abbreviare per fare prima in carta.",
            ),
            (
                "Quando smetto di ridurre?",
                "Quando la salsa copre il dorso del cucchiaio e resta, "
                "calda, lucida, continua. Se è ancora lunga, non è pronta. "
                "Se a freddo gelifica come una glace, sei andato oltre e "
                "hai un altro prodotto. Il punto nappante è la chiusura "
                "della demi-glace. Poi, al passe, la scaldi e se vuoi luce "
                "la mantechi, senza spingerla di nuovo.",
            ),
        ],
        "alt": [
            "Demi-glace scura che copre il dorso del cucchiaio e non scorre come un fondo",
            "Salsa spagnola e fondo bruno nella stessa pentola, in riduzione verso il nappante",
            "Carne al passe vestita da un velo di demi-glace, senza diventare glace",
        ],
        "tags": '["demi-glace", "salse", "fondo bruno", "tecnica di cucina"]',
        "links": [
            ("glace", "la glace de viande"),
            ("roux", "il roux bruno"),
            ("napar", "la prova nappante"),
        ],
    },
}


def _words(s: str) -> int:
    import re

    return len(re.findall(r"\S+", s))


if __name__ == "__main__":
    import re
    import sys

    ids = [
        "manie", "napar", "montar", "blanc", "gastrique", "yema",
        "glace", "fumet", "papilla", "roux", "emulsion", "demi",
    ]
    spellings = [
        "beurre manie", "beurre manié", "nappante", "napper", "mantecare",
        "monter au beurre", "burro bianco", "beurre blanc", "gastrique",
        "agrodolce", "legante al tuorlo", "glace de viande", "fumetto",
        "fumet", "amido", "emulsione", "demi-glace", "demiglace",
    ]
    bad = re.compile(
        r"\d|gramm|minut|°|%|€|Larousse|temperatur|percent",
        re.I,
    )
    voice = ("il passe", "la mise en place", "il margine", "il commensale")
    err = 0
    blob_busca = []
    for i in ids:
        c = COPY[i]
        blob = " ".join([c["lead"], *c["paras"], c["busca"], c["title"], c["description"]])
        for q, a in c["faq"]:
            blob += " " + q + " " + a
        print(f"== {i} ==")
        n = _words(c["lead"])
        mark = "" if 45 <= n <= 58 else " FUORI"
        print(f"  lead {n}{mark}")
        err += bool(mark)
        for j, p in enumerate(c["paras"], 1):
            n = _words(p)
            mark = "" if 85 <= n <= 110 else " FUORI"
            print(f"  p{j} {n}{mark}")
            err += bool(mark)
        n = _words(c["busca"])
        mark = "" if 60 <= n <= 90 else " FUORI"
        print(f"  busca {n}{mark}")
        err += bool(mark)
        d = len(c["description"])
        mark = "" if 140 <= d <= 165 else " FUORI"
        print(f"  desc {d}{mark}")
        err += bool(mark)
        for k, (q, a) in enumerate(c["faq"], 1):
            n = _words(a)
            mark = "" if 35 <= n <= 70 else " FUORI"
            print(f"  faq{k} {n}{mark}")
            err += bool(mark)
        blob_busca.append(c["busca"])
        if bad.search(blob):
            print("  BAD", bad.findall(blob)[:8])
            err += 1
        low = blob.lower()
        for v in voice:
            if v not in low and v not in blob:
                # il passe may appear with capital
                if v not in blob.lower():
                    print("  manca", v)
                    err += 1
    all_b = "\n".join(blob_busca)
    # fumet is a prefix of fumetto; require a standalone fumet too
    for s in spellings:
        if s == "fumet":
            if not re.search(r"\bfumet\b", all_b):
                print("manca grafia", s)
                err += 1
        elif s not in all_b:
            print("manca grafia", s)
            err += 1
    print("errori", err)
    sys.exit(1 if err else 0)
