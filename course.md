# Progettare e gestire le soluzioni AI in azienda


## Modulo 01: IA nei progetti: leve e criticità
### Scheda rapida del modulo
- **Leve di valore IA:** automazione e produttività, collaborazione uomo-IA, personalizzazione, innovazione, semplificazione dei processi.
- **Criticità da presidiare:** IA fine a sé stessa, qualità dati, rischio errore, responsabilità, integrazione su sistemi esistenti.
- **Scenari di integrazione:** IA come componente aggiuntiva, IA come motore centrale del prodotto, IA come abilitatore interno.
- **Prioritizzazione:** valutare sempre impatto utente, valore di business e fattibilità tecnica con criteri espliciti.
- **Esecuzione:** scegliere approccio cauto o rapido in base a rischio, conformità normativa e costo del fallimento.
- **Obiettivo didattico:** progettare una distribuzione efficace del lavoro tra IA e persone, con responsabilità chiare.

### Definire lo spazio di valore AI
In un progetto AI la domanda iniziale non è "quale modello usiamo?", ma "quale problema risolviamo e come misuriamo il miglioramento". Il valore reale emerge quando una soluzione aumenta le performance, riduce i costi operativi o migliora in modo visibile l'esperienza utente. Scoprire e definire problemi che valga la pena risolvere con l'IA è un'attività complessa che richiede di bilanciare obiettivi strategici a lungo termine e vittorie rapide.

Per impostare correttamente la scoperta delle opportunità, il processo si articola in tre passaggi fondamentali:
- **Individuare opportunità:** identificare aree dove l'IA può aggiungere valore partendo da indicazioni degli utenti e avanzamenti tecnologici.
- **Dare priorità alle opportunità:** valutare fattibilità tecnica, impatto e allineamento con gli obiettivi di business.
- **Dare forma alle opportunità:** dare forma alle opportunità esplorando approcci risolutivi e raffinando i concetti in caratteristiche concrete.

![Il processo di scoperta delle opportunità AI](assets/chapt02_images/ch02_p02_01.jpg)
*Figura M1.1: Il processo per scoprire le opportunità AI*

### Esempio operativo: servizio streaming musicale
Un esempio utile è la progettazione di un'app di streaming musicale orientata alla crescita dell'ascolto e alla riduzione dell'abbandono (churn). L'albero delle opportunità aiuta a partire dall'obiettivo di business e a scomporlo in opportunità concrete su cui intervenire con l'IA.

Nel caso streaming, il ramo "coinvolgimento" può includere raccomandazioni personalizzate, playlist dinamiche e suggerimenti contestuali in base al momento della giornata. Il ramo "fidelizzazione" può invece includere rilevazione anticipata di segnali di abbandono, campagne proattive e ottimizzazione dell'esperienza di onboarding musicale.

L'utilità pratica dell'albero è che rende esplicito il collegamento tra metrica di risultato e scelte di prodotto: ogni opportunità può essere valutata su impatto utente, valore di business e fattibilità tecnica prima di passare allo sviluppo.

![Albero delle opportunità AI per un'app di streaming musicale](assets/chapt02_images/image.png)
*Figura M1.2: Albero delle opportunità AI per un'app di streaming musicale*

### Leve di valore: come l'IA impatta i processi
La progettazione efficace parte dalla comprensione dei benefici attesi. Le sei tipologie principali di vantaggi includono:

**1. Automazione e produttività:** l'IA eccelle nel gestire compiti ripetitivi che richiedono molte piccole decisioni (es. servizio clienti, rilevamento frodi). Il valore è tangibile quando il costo del processo IA (sviluppo + esecuzione + gestione errori) è significativamente inferiore al costo del processo manuale.

![Equazione del costo AI per l'automazione](assets/chapt02_images/ch02_p05_01.jpg)
*Figura M1.3: L'equazione dei costi per le opportunità di automazione*

**2. Miglioramento e affiancamento:** anziché sostituire l'uomo, l'IA collabora portando i propri punti di forza (elaborazione dati su larga scala, precisione in domini definiti) a supporto delle capacità umane (comprensione del contesto, creatività, intelligenza emotiva).

![Punti di forza Umani vs AI](assets/chapt02_images/ch02_p06_01.jpg)
*Figura M1.4: Forze umane e dell'IA a confronto nella progettazione del prodotto*

**3. Personalizzazione:** adattare prodotti e servizi alle preferenze individuali utilizzando i dati sul comportamento degli utenti. Una buona personalizzazione richiede una solida base dati e un raffinamento continuo per non alienare l'utente con suggerimenti irrilevanti o invasivi.

**4. Ispirazione e innovazione:** l'IA può trasformare i processi di innovazione accelerando il ciclo idea-azione e analizzando pattern complessi in grandi volumi di dati (es. scoperta di nuovi materiali o farmaci).

**5. Comodità:** ridurre l'attrito nei percorsi utente eliminando passaggi noiosi, come nel caso di ricerche vocali intelligenti o sistemi di pianificazione automatica.

**6. Benefici emotivi:** creare interazioni che risuonano a livello personale, come assistenti vocali che comprendono il tono o motori di raccomandazione che colgono sfumature emotive sottili.

### Quando non usare AI: due regole pratiche
Non tutte le decisioni sono buoni candidati per l'automazione:
- **Decisioni rare o una tantum:** il costo di progettazione e mantenimento può superare il beneficio.
- **Spiegabilità totale obbligatoria:** in processi che richiedono motivazioni lineari e completamente tracciabili (es. procedure legali o creditizie ad alto impatto), approcci basati su regole o ibridi possono essere più adatti.

### Criticità e Scenari di Integrazione
Esistono tre scenari principali per integrare l'IA in un'azienda:
- **IA come componente aggiuntiva:** aggiornamento di un prodotto esistente (es. aggiungere funzionalità di reporting sostenibile a uno strumento esistente). Richiede grande attenzione alla gestione di dati frammentati e all'esperienza utente.
- **IA come motore di valore centrale:** l'IA è il motore primario della proposta di valore (scenari "greenfield"). Necessita di investimenti in raccolta dati di alta qualità fin dall'inizio.
- **IA come abilitatore interno:** ottimizzazione dei processi operativi "dietro le quinte" (es. segmentazione clienti più precisa per il marketing). Richiede metriche di efficienza chiare.

![Tre scenari di integrazione AI](assets/chapt02_images/ch02_p15_01.jpg)
*Figura M1.5: Scenari di integrazione AI: componente aggiuntiva, motore centrale, abilitatore interno*

### Caso studio: Miro
Miro rappresenta un caso utile di integrazione IA in un prodotto già adottato su larga scala per collaborazione visuale. L'AI non sostituisce il flusso di lavoro principale, ma accelera attività ad alto volume cognitivo: sintesi dei contenuti, riorganizzazione delle idee, generazione di prime bozze e supporto alla convergenza decisionale nei workshop.

Dal punto di vista progettuale, il valore nasce dall'inserimento dell'AI nel punto in cui il team perde più tempo: passare da molti input disordinati a una struttura condivisa e azionabile. In questo schema, la componente umana resta decisiva per priorità, qualità delle decisioni e validazione finale.

Questo caso studio mostra bene un principio generale: l'IA genera ROI quando riduce il tempo tra esplorazione e allineamento operativo senza compromettere controllo, trasparenza e qualità dell'output.

Link di riferimento: [Miro](https://miro.com/)

![Caso studio Miro](assets/chapt02_images/miro.png)
*Figura M1.6: Esempio di integrazione AI in Miro per la collaborazione di team*

### Tre modalità di integrazione nei prodotti
1. **IA come componente aggiuntiva** su prodotto esistente.
2. **IA come motore centrale** di un prodotto nativamente IA.
3. **IA come abilitatore interno** per ottimizzare processi operativi.

Nel modello a componente aggiuntiva il vantaggio è la velocità sul mercato grazie a base utenti e processi già presenti; la sfida è integrare senza degradare esperienza utente e fiducia. Nel modello nativamente IA la priorità è costruire qualità del modello e dei dati in tempi rapidi. Nel modello interno il focus è ROI operativo: efficienza, sicurezza dei dati, adozione dei team e continuità di utilizzo.

### Fonti di opportunità AI: costruire un flusso continuo
Per avere un flusso solido di idee non basta aspettare richieste dai clienti. Serve un sistema continuo di scoperta che combini segnali interni ed esterni.

#### Conoscenza interna e intuizione esperta
Team di prodotto, design, vendita e operazioni hanno conoscenza operativa del dominio. Questa esperienza permette di generare ipotesi ad alta velocità, purché siano validate presto con test reali.

#### Uso interno e sperimentazione
Usare internamente le funzionalità AI accelera i cicli di apprendimento perché i feedback arrivano subito. È un'ottima fase iniziale, ma non deve durare troppo: dopo il primo MVP è necessario validare con utenti esterni per evitare distorsioni.

#### Ascolto clienti e dati comportamentali
Interviste, ticket, recensioni e analisi vanno letti insieme. Le dichiarazioni degli utenti sono utili, ma il comportamento osservato in prodotto è il controllo di realtà che evita decisioni basate su percezioni parziali.

#### Segnali esterni di mercato
Le opportunità più difendibili spesso emergono da quattro segnali:
1. **Nuovi avanzamenti tecnologici:** aprono possibilità prima non fattibili.
2. **Mosse dei concorrenti:** aiutano a capire cosa il mercato è già disposto ad adottare.
3. **Regolamentazioni:** creano nuovi processi obbligatori e quindi nuovi bisogni di automazione.
4. **Posizionamento strategico:** in alcuni casi l'IA rafforza il posizionamento innovativo, ma deve sempre restare collegata a valore reale per il cliente.

#### Opportunità concreta: modernizzazione sistemi legacy (COBOL)
Un'area ad alto valore è la modernizzazione di applicazioni legacy in COBOL con supporto IA: il valore non è solo tecnico, ma economico e strategico. In molti contesti, la migrazione riduce costi ricorrenti di licenze e dipendenze da stack proprietari, con minore lock-in tecnologico e maggiore flessibilità evolutiva.

Riferimento di mercato: [IBM stock suffers worst single-day drop in 25 years over Anthropic's COBOL tool](https://timesofindia.indiatimes.com/technology/tech-news/ibm-stock-suffers-worst-single-day-drop-in-25-years-over-anthropics-cobol-tool-what-it-is-and-why-it-wiped-billions-of-dollar-for-ibm/articleshow/128744951.cms).

### Opportunità orizzontali vs verticali
Distinguere presto questo punto evita errori di strategia:
- **Orizzontali:** risolvono bisogni trasversali a molti settori (es. scrittura assistita, supporto al lavoro della conoscenza).
- **Verticali:** risolvono problemi specifici di un settore (es. finanza, sanità, assicurazioni), richiedendo più competenza di dominio e spesso messa a punto mirata dei modelli.

Operativamente, i casi orizzontali richiedono forte capacità di scalare il prodotto su mercati eterogenei; i casi verticali richiedono maggiore profondità su normativa, processi e linguaggio specialistico.

#### Riferimento consigliato: McKinsey 2023
McKinsey nel 2023 ha evidenziato il tema nel report "The Economic Potential of Generative AI: The Next Productivity Frontier" ([link](https://mng.bz/vZla)).

Riassunto operativo su orizzontale/verticale:
- **Orizzontale:** una quota molto rilevante del valore GenAI si concentra in funzioni trasversali presenti in quasi tutte le aziende, in particolare operazioni con i clienti, marketing e vendite, ingegneria del software, ricerca e sviluppo.
- **Verticale:** alcuni settori mostrano potenziale relativo più alto rispetto ai ricavi (tra cui bancario, alta tecnologia, scienze della vita), perché combinano intensità informativa, processi ad alta intensità di conoscenza e casi d'uso ad alta leva.
- **Implicazione progettuale:** se cerchi adozione rapida e scala, parti da casi d'uso orizzontali; se cerchi differenziazione difendibile, investi in casi d'uso verticali con forte integrazione di dominio e dati proprietari.

### Capacità dell'IA generativa e dei GPT: casi d'uso, punti deboli e rischi
La GenAI non è una singola funzionalità ma una famiglia di capacità che copre testo, immagini, video, codice, audio e automazione cognitiva. Per progettare bene serve separare tre livelli: **cosa può fare**, **dove conviene usarla**, **quali rischi comporta**.

#### Capacità operative principali
- **Generazione testuale:** scrittura di contenuti, assistenza conversazionale, traduzione, sintesi.
- **Generazione visiva e multimediale:** creazione immagini realistiche/stilizzate, editing video, effetti e supporto alla modellazione 3D.
- **Supporto allo sviluppo software:** generazione snippet, refactoring assistito, documentazione tecnica, aiuto nel testing.
- **Output creativi aggiuntivi:** supporto a composizione musicale, script e varianti di stile.
- **Adattabilità al contesto:** modelli pre-addestrati che possono essere specializzati su compiti specifici tramite istruzioni, contesto e adattamento mirato (fine-tuning).

#### Casi d'uso da presidiare in azienda
| Area | Casi d'uso concreti | Valore atteso |
| --- | --- | --- |
| Contenuti e marketing | descrizioni prodotto, post social, campagne, tagline, varianti copy | maggiore velocità di produzione, riduzione tempo di immissione sul mercato |
| Giornalismo e lavoro della conoscenza | sintesi report, bozze articoli, supporto verifica fattuale preliminare | accelerazione attività redazionali e analitiche |
| Servizio clienti | chatbot, risposte automatiche, raccomandazioni contestuali | riduzione tempi risposta e migliore copertura servizio |
| Educazione e formazione | piani personalizzati, quiz, spiegazioni multi-formato, pratica conversazionale linguistica | apprendimento più personalizzato e scalabile |
| Industrie creative | bozzetti creativi, storyboard, effetti video, musica, supporto progettazione di giochi e dialoghi NPC | espansione capacità creativa e prototipazione rapida |
| Ingegneria del software | generazione codice, commenti/documentazione, casi di test e dati sintetici | aumento produttività del team e qualità dei cicli di rilascio |
| Sanità | supporto analisi immagini, aiuto a scoperta farmacologica, personalizzazione trattamenti | migliore supporto decisionale clinico e priorità operative |
| Finanza | reportistica automatica, sintesi dati mercato, supporto rilevazione frodi | più velocità su analisi e controllo del rischio |
| Ricerca scientifica | sintesi letteratura, ipotesi iniziali, supporto disegno sperimentale | riduzione tempo di esplorazione e revisione conoscenza |

#### Punti deboli tecnici e qualitativi
- **Errori fattuali plausibili:** il modello può formulare risposte fluenti ma non corrette, soprattutto su domini specialistici.
- **Distorsioni nei dati di addestramento:** output distorti o discriminatori se non si applicano controlli di equità.
- **Debolezza su ragionamento profondo:** buona capacità statistica, ma comprensione semantica e giudizio causale limitati.
- **Tenuta ridotta su testi lunghi:** possibili incoerenze su output estesi, con perdita di struttura logica.
- **Rischio di omologazione contenuti:** uso eccessivo può produrre testi generici e poco distintivi.
- **Problema autenticità:** distinguere contenuti umani e sintetici è sempre più difficile, con impatti su fiducia e tracciabilità.
- **Dipendenza dalla qualità dati:** senza dati e prompt di qualità, la performance degrada rapidamente.

#### Rischi principali da includere nel framework di governance
| Categoria rischio | Descrizione operativa | Impatto potenziale | Strategia di mitigazione |
| --- | --- | --- | --- |
| Qualità e affidabilità | allucinazioni, incompletezza, errori di contesto | decisioni errate, costi operativi, danno cliente | supervisione umana nel ciclo (human-in-the-loop) sugli output critici, verifica fattuale obbligatoria, test e validazione su dataset reali |
| Sicurezza e abuso | phishing generativo, ingegneria sociale, deepfake, supporto a codice malevolo | frodi, incidenti cyber, danni reputazionali | controlli di sicurezza su prompt e output, politiche anti-abuso, monitoraggio continuo e risposta agli incidenti |
| Etica e legale | proprietà intellettuale, attribuzione, disinformazione, opacità verso utenti | contenziosi, violazioni di policy, perdita credibilità | linee guida etiche interne, revisione legale dei casi sensibili, trasparenza sull'uso dell'IA verso utenti e stakeholder |
| Conformità e regolazione | mancato rispetto obblighi su trasparenza, uso dati, governance dell'IA | sanzioni, blocchi progetto, aumento rischio legale | politiche di governance formalizzate, responsabilità su ruoli e decisioni, aggiornamento continuo rispetto a normative e standard |
| Fiducia e brand | output offensivi, fuorvianti o manipolativi in touchpoint pubblici | perdita fiducia clienti e impatto commerciale | controlli editoriali di qualità, supervisione umana nei contenuti pubblici, comunicazione trasparente quando il contenuto è assistito dall'IA |
| Organizzazione e lavoro | sostituzione parziale attività, disallineamento competenze, adozione disordinata | resistenza interna, inefficienza, calo qualità decisionale | piano di formazione, adozione progressiva per casi d'uso ben definiti, responsabilità esplicita su revisione e responsabilità finale |

#### Strategie chiave per usare l'IA generativa e i GPT
| Strategia chiave | Obiettivo operativo | Azioni pratiche |
| --- | --- | --- |
| Partire da casi d'uso ben definiti | evitare iniziative "IA fine a sé stessa" e concentrarsi su valore misurabile | partire da problemi concreti, iniziare con progetti piccoli, valutare ROI e costo totale di adozione |
| Puntare sulla collaborazione uomo-AI | usare l'IA come amplificatore del lavoro umano, non come sostituto integrale | mantenere supervisione umana continua, formare i team, preservare responsabilità decisionale umana |
| Dare priorità a controllo qualità e mitigazione dei bias | ridurre errori, allucinazioni e output distorti | test e validazione su dataset reali, verifica fattuale strutturata, controlli periodici di bias su prompt e output |
| Rafforzare trasparenza e responsabilità | aumentare fiducia interna/esterna e chiarezza delle responsabilità | dichiarare quando l'IA è usata, definire responsabili di processo, adottare politiche di sviluppo, rilascio e monitoraggio |
| Investire in sperimentazione e apprendimento continuo | adattarsi all'evoluzione rapida di modelli, tecniche e regolazione | cicli continui di test e apprendimento, aggiornamento competenze, monitoraggio normativo proattivo |
| Rafforzare basi dati e sicurezza | mantenere qualità dell'output e ridurre rischio operativo/cyber | curare qualità dati e dataset per il fine-tuning, proteggere accessi e modelli, controllare uso e abuso delle integrazioni |

### Esempio negativo: IA fine a sé stessa (caso Sanremo 2026)
Un esempio utile di cosa **non** fare è il caso riportato da Fanpage il **25 febbraio 2026** sulla regia di Sanremo: un effetto visivo generato con IA, inserito durante la diretta, è stato percepito come scadente e fuori contesto rispetto al livello atteso dell'evento. Vai direttamente all'articolo con video: [Fanpage - La regia di Sanremo ha usato per la prima volta l'IA, ma è stato un incubo](https://www.fanpage.it/innovazione/tecnologia/la-regia-di-sanremo-ha-usato-per-la-prima-volta-lia-ma-e-stato-un-incubo-cosa-non-ha-funzionato/).

L'esempio mostra il classico anti-pattern "AI for the sake of AI": usare IA solo per dimostrare che la si sta usando, senza un reale miglioramento dell'esperienza.

Errori da evitare:
- inserire una funzionalità IA senza obiettivo utente misurabile;
- non definire una soglia minima di qualità prima della messa in onda;
- usare effetti "novità" non coerenti con il contesto operativo e reputazionale;
- non prevedere un meccanismo di fallback immediato verso una regia tradizionale.

Lezione operativa:
- prima di introdurre IA in un touchpoint pubblico, chiarire quale problema risolve;
- validare la qualità in condizioni reali;
- assegnare responsabilità esplicite su approvazione finale e gestione incidenti.

#### Devo usare l'IA generativa o i GPT per operazioni di business critiche?
| Punto chiave | Implicazione operativa |
| --- | --- |
| non affidare decisioni critiche esclusivamente a GPT/GenAI | usare i modelli come supporto, non come decisore finale |
| mancanza di comprensione causale e limiti nel giudizio contestuale | richiedere revisione esperta umana nei passaggi ad alto impatto |
| possibili distorsioni nei dati di addestramento | applicare controlli di equità e verifiche su gruppi sensibili |
| errori fattuali plausibili in domini specialistici | introdurre verifica fattuale strutturata e validazione su fonti autorevoli |
| responsabilità poco chiara se la decisione è affidata solo all'IA | assegnare responsabilità esplicita su decisione, approvazione ed escalation |
| analisi di grandi volumi dati e individuazione pattern | usare output AI per pre-analisi e supporto alle ipotesi decisionali |
| generazione di scenari alternativi | supportare workshop decisionali e confronto alternative |
| sintesi di report complessi | accelerare comprensione manageriale senza saltare la verifica |
| collaborazione uomo-IA con supervisione umana nel ciclo (human-in-the-loop) | combinare velocità AI con pensiero critico, giudizio etico e responsabilità umana |

#### Identificare e gestire i rischi di fallimento nell'implementazione della strategia AI
| Fallimenti comuni della strategia AI | Tattiche di mitigazione |
| --- | --- |
| Obiettivi disallineati: progetti AI senza obiettivi business chiari o scollegati da problemi reali | partire da uno scopo esplicito, collegando ogni iniziativa alla missione e alle priorità aziendali |
| Qualità insufficiente delle fonti dati: dati incompleti, distorti o non affidabili | rafforzare la data governance con controlli qualità, gestione robusta del dato e mitigazione bias lungo il ciclo di vita |
| Carenza di competenze: team senza competenze adeguate su dati, dominio e AI responsabile | costruire il team corretto con assunzioni mirate, formazione e partnership esterne |
| Sottostima della complessità: tempi, costi e difficoltà tecniche valutati in modo troppo ottimistico | impostare aspettative realistiche su piano evolutivo, budget e performance, favorendo sperimentazione e apprendimento |
| Presidio etico tardivo: equità, privacy e responsabilità trattate solo a valle | integrare etica e controlli di rischio fin dalla progettazione |
| Resistenza al cambiamento: scarso coinvolgimento di stakeholder e team operativi | comunicare in modo trasparente benefici e limiti dell'IA per creare fiducia e adozione |
| Sviluppo a silos: funzioni che lavorano isolate senza coordinamento interfunzionale | abilitare collaborazione tra data science, IT, business, rischio/conformità ed esperti etici |
| Mancata capacità di pivot: persistenza su piani non efficaci nonostante feedback contrari | adottare un approccio adattivo con revisioni periodiche, correzione rotta e iterazioni guidate dai dati |
| Sponsorship esecutiva debole: supporto insufficiente del top management | ottenere impegno della leadership per risorse, priorità e rimozione degli ostacoli organizzativi |

#### Definire la responsabilità per i sistemi di IA
La responsabilità nei sistemi di IA richiede responsabilità esplicite su progettazione, rilascio, uso e gestione degli impatti. Nei contesti reali, il modello attraversa più team e fasi: senza una catena di responsabilità chiara, ogni incidente produce ritardi, conflitti e decisioni poco tracciabili.

| Livello di responsabilità | Responsabilità primaria |
| --- | --- |
| Sviluppatori e data scientist | architettura tecnica, selezione dati, addestramento, valutazione iniziale, presidio di equità e robustezza |
| Team di rilascio e operazioni | messa in esercizio, monitoraggio in produzione, gestione effetti inattesi e allineamento all'uso previsto |
| Organizzazione (entità legale) | governance complessiva, definizione rischio accettabile, meccanismi di remediation e conformità |
| Funzioni di controllo/regolatori | definizione regole, verifica conformità, applicazione delle regole e richieste di adeguamento |

Meccanismi operativi da attivare:
- **trasparenza e spiegabilità:** rendere comprensibili basi e limiti delle decisioni AI;
- **tracciabilità di audit e documentazione:** tracciare dati, versioni modello, decisioni e approvazioni;
- **processi di contestazione e riesame:** permettere contestazione strutturata degli esiti ad alto impatto;
- **supervisione indipendente:** audit periodici su sistemi critici con verifica controlli e gap;
- **governo legale e conformità:** aggiornare policy e controlli in base all'evoluzione normativa.

#### Regola di impiego nei processi critici
Nei processi ad alto impatto, la GenAI va usata come **copilota** e non come decisore unico. Le attività in cui è molto utile sono:
- analisi preliminare di grandi volumi informativi;
- generazione di scenari alternativi;
- sintesi per facilitare decisioni manageriali.

La decisione finale deve restare umana, con responsabilità esplicita su verifica fattuale, valutazione etica, gestione delle distorsioni e tracciabilità delle responsabilità.

### Prioritizzazione: decidere bene con criteri espliciti
Per non cadere nella trappola dell'analisi infinita ("paralisi da analisi"), è fondamentale usare criteri stabili e condivisi su cui confrontare le opportunità.

![Ramo personalizzazione nell'albero delle opportunità](assets/chapt02_images/ch02_p20_01.jpg)
*Figura M1.7: Focus sul ramo personalizzazione da valutare in fase di prioritizzazione*

I tre assi base restano:
1. **Impatto utente:** quanto valore crea per il cliente finale?
2. **Valore di business:** come contribuisce agli obiettivi aziendali (es. riduzione dell'abbandono (churn), nuovi ricavi)?
3. **Fattibilità tecnica:** abbiamo i dati, i modelli e le competenze per realizzarlo?

Nel caso streaming, un motore di raccomandazione può avere alto impatto perché migliora scoperta e fidelizzazione; la fattibilità aumenta se esistono già dati storici su ascolti, skip, like e playlist. Al contrario, funzionalità come ricerca vocale avanzata possono avere valore ma richiedere costi e complessità più elevati nella fase iniziale.

Accanto ai tre assi generali è utile aggiungere criteri specifici al contesto:
- **Facilità regolatoria** in settori ad alta conformità normativa.
- **Prontezza dei dati** quando la qualità o disponibilità dei dati è il collo di bottiglia principale.
- **Scalabilità e personalizzazione** quando la soluzione va distribuita su clienti aziendali eterogenei.

![Matrice di prioritizzazione AI](assets/chapt02_images/ch02_p22_01.jpg)
*Figura M1.8: Esempio di matrice per la valutazione delle opportunità AI*

I punteggi aiutano a rendere esplicito il ragionamento, ma non devono sostituire il giudizio di prodotto. La prioritizzazione migliore è quella che rende chiari rischi, assunzioni e condizioni di cambio rotta.

### Bilanciare risultati rapidi e investimenti a lungo termine
Un piano evolutivo robusto combina:
- **Risultati rapidi:** rilascio veloce, apprendimento rapido, impatto immediato.
- **Investimenti difendibili:** iniziative più lunghe che costruiscono vantaggio competitivo nel tempo.

Concentrarsi solo sui risultati rapidi porta risultati rapidi ma facilmente imitabili. Concentrarsi solo sul lungo termine rallenta l'apprendimento e aumenta il rischio di investimenti non validati. L'equilibrio dipende dal ruolo dell'AI nella strategia aziendale.

### Strategie di esecuzione: cauto vs rapido
La scelta dell'approccio dipende da rischio, costo del fallimento e contesto regolatorio.

- **Approccio Cauto (Pronto, mira, fuoco):** ricerca approfondita, validazione forte di impatto, fattibilità e conformità prima dello sviluppo. È adatto quando errore e non conformità hanno costo molto alto.
- **Approccio Rapido (Pronto, fuoco, mira):** prototipazione veloce, test con utenti reali, iterazioni frequenti. È adatto quando il costo iniziale è basso, il mercato è veloce e il feedback reale è il principale riduttore di incertezza.

![Confronto approccio cauto vs rapido](assets/chapt02_images/ch02_p24_01.jpg)
*Figura M1.9: Confronto tra approccio cauto e rapido nella realizzazione AI*

Nel flusso cauto, il team documenta in anticipo impatto, fattibilità e vincoli per ridurre il rischio di decisioni irreversibili in contesti critici.

![Processo design thinking per approccio cauto](assets/chapt02_images/ch02_p25_01.jpg)
*Figura M1.10: Processo tipico dell'approccio cauto (empatizzare, definire, ideare, prototipare, testare)*

Nel flusso rapido, il team costruisce presto una soluzione completa funzionante per validare ipotesi con dati reali. Questo approccio funziona bene quando la soluzione richiede più cicli di messa a punto e il comportamento utente non è prevedibile solo da analisi teorica.

### Principali punti di fine sezione
- costruire un flusso continuo di opportunità da più fonti, non solo da una;
- scegliere consapevolmente tra opportunità orizzontali e verticali;
- valutare con criteri stabili, trasparenti e coerenti nel tempo;
- bilanciare risultati rapidi e vantaggio competitivo di lungo periodo;
- adottare approccio cauto o rapido in base a rischio, conformità normativa, costo del fallimento e cultura del team.

### Mappare lo spazio della soluzione AI
Per non perdersi nella vastità di modelli e strumenti rilasciati quotidianamente, è necessario costruire una mappa strutturata che guidi la scoperta della soluzione. Lo spazio della soluzione si articola su tre componenti fondamentali: **dati**, **intelligenza** ed **esperienza utente (UX)**, tutti circondati da un livello di **governance**.

![Mappa dello spazio della soluzione AI](assets/chapt03_images/ch03_p02_01.jpg)
*Figura M1.11: Mappa dello spazio della soluzione nel modello mentale di un sistema AI*

Una categorizzazione sistematica aiuta a comunicare con stakeholder tecnici e non, a valutare le competenze necessarie e a comprendere come le scelte in un ambito (es. i dati) influenzino gli altri (es. l'intelligenza o l'interfaccia).

![Categorizzazione dello spazio della soluzione AI](assets/chapt03_images/ch03_p03_01.jpg)
*Figura M1.12: Categorizzazione dettagliata dello spazio della soluzione AI*

**Nota: cosa significa "Neuro-symbolic AI"**
La **Neuro-symbolic AI** è un approccio ibrido che combina:
- **IA neurale:** modelli statistici (es. deep learning) molto efficaci nell'apprendere dai dati;
- **IA simbolica:** regole e logica esplicita (if-then, ontologie, vincoli), utile per ragionamento strutturato e tracciabilità.

In pratica, la parte neurale propone o predice, mentre la parte simbolica controlla, vincola o spiega secondo regole di dominio. È utile quando servono insieme prestazioni del modello, controllo operativo, spiegabilità e conformità.

### 1. Dati: il carburante del sistema
I dati non sono più solo un tema ingegneristico, ma impattano direttamente l'esperienza utente. Devono riflettere i bisogni reali e non solo la procedura di addestramento.

#### La modalità dei dati
Le modalità rappresentano i diversi tipi di dati da cui i modelli imparano:
- **Testuale:** focalizzata su elaborazione e generazione di linguaggio naturale (NLP). Include compiti come sentiment analysis, traduzione e sintesi.
- **Visiva:** gestione di immagini e video tramite computer vision per estrarre caratteristiche e riconoscere oggetti.
- **Auditiva:** riconoscimento vocale, biometria vocale e analisi delle emozioni basata sull'intonazione.
- **Sensorimotoria:** dati raccolti dal mondo fisico tramite sensori, fondamentale per robotica, droni e domotica.
- **Codice informatico:** un linguaggio altamente formalizzato che abilita l'automazione dello sviluppo e aumenta la produttività dei programmatori.

Indipendentemente dalla fonte, l'IA trasforma sempre i dati grezzi in una **modalità numerica** (vettori) per poterli elaborare matematicamente.

![Relazioni tra le modalità AI](assets/chapt03_images/ch03_p04_01.jpg)
*Figura M1.13: Relazioni tra le modalità grezze e la trasformazione in modalità numerica*

Questa trasformazione (preprocessing) è un atto strategico: una rappresentazione troppo grossolana, come la *one-hot encoding*, può far perdere informazioni cruciali sull'importanza e sul contesto delle parole.

![Esempio di codifica one-hot](assets/chapt03_images/ch03_p06_01.jpg)
*Figura M1.14: La codifica one-hot come rappresentazione numerica algebrica delle parole*

L'attuale frontiera è l'**IA Multimodale**, che combina più sensi (es. vista e udito) per costruire un contesto più ricco e accurato, proprio come fa il cervello umano nel processo di apprendimento.

#### Dati etichettati vs Non etichettati
- **Dati non etichettati:** privi di segnali di apprendimento espliciti (usati per il clustering). Poiché i risultati sono incerti, vengono raramente usati da soli in applicazioni consumer finali.
- **Dati etichettati:** ogni punto è associato a un "label" che indica l'obiettivo desiderato (es. recensione "positiva", immagine di "gatto"). Forniscono un segnale di apprendimento chiaro e preciso (apprendimento supervisionato).

Un caso particolare sono i **Large Language Models (LLM)**: sebbene usino volumi di dati enormi, utilizzano un trucco di auto-etichettatura dove la "parola successiva" funge da etichetta per la sequenza che la precede, permettendo l'addestramento su scala planetaria.

### 2. Tipi di intelligenza: dai simboli agli agenti
Il paradigma di intelligenza scelto dipende dalla natura e complessità del problema da risolvere.

#### IA basata su regole (simbolica)
Si basa su logica, database e ontologie create dall'uomo. È ideale quando il dominio è normativo, stabile e trasparente (es. controlli legali nel banking).
- **Vantaggi:** avvio rapido per un MVP, spiegabilità totale degli output, aiuto fondamentale nella raccolta di dati strutturati per iterazioni future.
- **Svantaggi:** copertura limitata; la realtà presenta troppe sfumature e casi limite per essere racchiusa interamente in regole rigide.

#### Apprendimento automatico (IA neurale)
Qui è la macchina a imparare dai dati. Si divide in tre paradigmi principali:

1. **IA Predittiva (Analitica):** si focalizza su compiti ben delimitati come previsioni future, trend e rilevamento anomalie. Aiuta a digerire grandi volumi di dati per estrarre indicazioni utili, ma richiede ancora un intervento umano per tradurre l'analisi in azione.
2. **IA Generativa:** crea nuove informazioni (testo, immagini, codice, musica) che somigliano ai pattern di addestramento. Funge da partner di confronto creativo e accelera le attività di routine.
3. **IA Agentica:** colma il divario tra indicazioni e azione. Non si limita a suggerire, ma esegue attività autonomamente tramite strumenti integrati (plugin software o dispositivi fisici), basandosi su catene di ragionamento generate da modelli linguistici.

![Esempi di problemi di apprendimento](assets/chapt03_images/ch03_p10_01.jpg)
*Figura M1.15: Esempi di problemi risolti da IA Predittiva, Generativa e Agentica*

Un esempio tipico di IA Predittiva è la trasformazione di feedback non strutturati in dati numerici strutturati (sentiment score) per supportare decisioni strategiche sul prodotto.

![Strutturazione di dati testuali con sentiment analysis](assets/chapt03_images/ch03_p11_01.jpg)
*Figura M1.16: Esempio di come l'IA trasforma testo non strutturato in dati quantitativi*

### 3. Esperienza utente: l'interfaccia del valore
L'interfaccia (UI) assicura che il valore creato dall'IA venga effettivamente consegnato all'utente in modo usabile e comprensibile.

#### Tipologie di interfacce AI
- **Conversazionali:** offrono massima flessibilità tramite il linguaggio naturale, ma soffrono della "barriera di articolazione" (gli utenti non sempre sanno cosa chiedere) e del rischio di allucinazioni.
- **Grafiche:** forniscono struttura, prevedibilità e fiducia, elementi critici soprattutto nei contesti B2B e analitici.
- **Ibride:** bilanciano flessibilità e controllo, integrando conversazione per input aperti e componenti grafici (pulsanti, menu) per azioni fisse e ben definite (es. diagnosi, rilascio).
- **Generative:** rappresentano il futuro, dove l'interfaccia si adatta dinamicamente al modello mentale dell'utente, personalizzando design e interazioni a ogni passo.

![ChatGPT: l'interfaccia conversazionale moderna](assets/chapt03_images/ch03_p16_01.jpg)
*Figura M1.17: ChatGPT come prototipo di interfaccia conversazionale*

![Interfaccia grafica B2B](assets/chapt03_images/ch03_p17_01.jpg)
*Figura M1.18: Innovation Monitor di Anacode: un'interfaccia grafica che fornisce contesto solido e fiducia*

![Interfaccia Ibrida](assets/chapt03_images/ch03_p18_01.jpg)
*Figura M1.19: Vercel v0.dev: esempio di interfaccia ibrida che combina chat e controlli strutturati*

#### Criteri pratici per interfacce ibride e generative
Quando un sistema AI entra in produzione, la scelta dell'interfaccia non è solo estetica: determina qualità operativa, velocità decisionale e rischio d'errore. Nelle attività ad alta variabilità conviene lasciare spazio alla conversazione, mentre nei passaggi a rischio (approvazione, rilascio, modifiche dati, escalation) serve una UI guidata con azioni esplicite.

Uno schema efficace è separare:
- **zona esplorativa:** prompt liberi, ipotesi, generazione di alternative;
- **zona di controllo:** pulsanti e flussi vincolati per azioni irreversibili;
- **zona di verifica:** evidenze, motivazioni, confidenza del sistema, possibilità di ripristino.

Questo assetto riduce la "barriera di articolazione", evita prompt troppo vaghi e mantiene tracciabilità nelle decisioni di prodotto.

### Gradi di automazione e collaborazione Uomo-IA
La progettazione di una collaborazione efficace tra umani e IA è il cuore della UX di un prodotto di successo.

#### I livelli di automazione
Si distinguono tre categorie principali:
1. **Intelligenza assistita (Assisted Intelligence):** l'IA supporta e potenzia le decisioni umane senza agire in autonomia (es. sistemi di allerta).
2. **Intelligenza aumentata (Augmented Intelligence):** l'IA automatizza parti significative del lavoro, ma richiede ancora supervisione umana per la validazione finale.
3. **Intelligenza autonoma (Autonomous Intelligence):** l'IA opera, decide e agisce in autonomia con intervento umano minimo o nullo.

![Livelli di automazione AI in diversi settori](assets/chapt03_images/ch03_p19_01.jpg)
*Figura M1.20: Esempi di applicazioni con diversi gradi di automazione in guida autonoma, sanità e servizio clienti*

#### Il caso guida: Guida Autonoma (Livelli SAE)
La transizione dall'assistenza all'autonomia totale è ben esemplificata dai 6 livelli SAE per i veicoli, che vanno dall'assenza di automazione (Livello 0) alla guida autonoma totale in ogni condizione (Livello 5).

![Livelli SAE di automazione della guida](assets/chapt03_images/ch03_p20_01.jpg)
*Figura M1.21: I livelli di automazione definiti da SAE International*

### Distribuzione ottimale del lavoro
Il successo di un prodotto IA dipende dal trovare la distribuzione del lavoro che massimizza i punti di forza di entrambi gli attori:

- **Punti di forza dell'IA:** elaborazione dati su scala massiva, rilevamento di pattern invisibili all'uomo, oggettività decisionale (assenza di emozioni), scalabilità immediata e operatività h24.
- **Punti di forza dell'Uomo:** intuizione profonda, intelligenza emotiva e abilità sociali, comprensione del contesto strategico e aziendale, adattabilità a nuovi scenari non strutturati e giudizio etico/morale.

Un prodotto AI eccellente non punta a eliminare l'uomo, ma a integrarsi nel suo flusso di lavoro per liberarlo dalle attività ripetitive, permettendogli di concentrarsi su attività ad alto valore aggiunto e criticità.

### IA predittiva applicata al prodotto: quadro operativo completo
Per molte aziende, la prima leva concreta non è la generazione di contenuti, ma la capacità di trasformare dati già disponibili in decisioni operative migliori. Un flusso predittivo ben disegnato permette di segmentare utenti, anticipare l'abbandono (churn), intercettare anomalie e aumentare conversione senza affidarsi a intuizioni isolate.

Nel seguito useremo un **caso e-commerce** come filo conduttore: un negozio online che vuole aumentare conversione e valore medio ordine, riducendo abbandono e spreco di campagne. I dati disponibili includono navigazione, ricerche, carrelli, acquisti e risposta alle raccomandazioni.

#### Ciclo iterativo: dal problema di business all'azione
Il lavoro efficace parte da domande di prodotto precise e misurabili. Nel caso e-commerce, la domanda non è "facciamo ML?", ma:
- quali utenti non convertono e perché;
- quali comportamenti anticipano abbandono;
- quali interventi hanno impatto reale su fidelizzazione e fatturato.

![Ciclo iterativo per sistemi predittivi ad alto valore](assets/chapt04_images/ch04_img03.png)
*Figura M1.22: ciclo iterativo di realizzazione per IA predittiva ad alto valore*

Il ciclo operativo utile in pratica:
1. **Formulazione del problema:** tradurre obiettivi di business in attività di apprendimento.
2. **Preparazione dati:** raccolta, trasformazione, pulizia, controllo qualità.
3. **Selezione algoritmi:** scegliere approccio coerente con il tipo di segnale.
4. **Valutazione tecnica e di impatto:** metriche modello + metriche di prodotto.
5. **Messa a terra operativa:** campagne, UX, processi decisionali, monitoraggio.

#### Apprendimento non supervisionato: segmentazione comportamentale
La segmentazione non supervisionata è un ottimo punto di ingresso quando il dataset è ricco ma ancora poco strutturato. Invece di segmentare solo per demografia, conviene costruire cluster su segnali di comportamento: frequenza visite, uso raccomandazioni, profondità del funnel, valore acquisti, editing profilo.

Esempio di struttura dati utile per clustering:

| user_id | purchased_items | purchase_value | last_active | n_visits |
| --- | --- | --- | --- | --- |
| abhj3k | 2 | 908 | 2024-04-30 08:36:24 | 48 |
| shj67d | 0 | 0 | 2023-12-26 12:56:24 | 24 |
| i963gh | 12 | 673 | 2024-05-15 23:22:11 | 156 |

La qualità dei cluster dipende da scelte pratiche:
- ingegnerizzazione iterativa delle caratteristiche, con rimozione delle variabili poco informative;
- standardizzazione delle caratteristiche per evitare distorsioni di scala;
- gestione di valori mancanti, duplicati, anomalie e distorsioni note in fase dati;
- minimizzazione dei dati sensibili e verifica del consenso d'uso.

![Clustering K-means e centroidi](assets/chapt04_images/ch04_img05.png)
*Figura M1.23: K-means con centroidi e aggregazione dei punti dati*

Per la scelta algoritmo:
- **K-means:** molto usabile, rapido, leggibile dal team di business;
- **gerarchico:** utile se vuoi esplorare granularità diverse senza fissare subito K;
- **DBSCAN:** efficace per forme irregolari e per isolare outlier.

Metriche minime da presidiare:
- **coefficiente di silhouette:** coesione interna e separazione tra cluster;
- **indice Calinski-Harabasz:** bontà della separazione complessiva.

#### Dal clustering alla classificazione supervisionata
Una volta individuati cluster utili, conviene stabilizzarli con classificazione supervisionata: i cluster diventano etichette e il modello assegna automaticamente i nuovi utenti al segmento corretto. In questo modo la segmentazione scala senza rilanciare clustering continuo.

Esempio di dataset etichettato:

| user_id | purchased_items | purchase_value | last_active | n_visits | search_queries | segment |
| --- | --- | --- | --- | --- | --- | --- |
| abhj3k | 2 | 908 | 2024-04-30 08:36:24 | 48 | 3 | Seekers |
| shj67d | 0 | 0 | 2023-12-26 12:56:24 | 24 | 45 | Conservatives |
| i963gh | 12 | 673 | 2024-05-15 23:22:11 | 156 | 25 | Indecisives |
| ty54df | 20 | 1250 | 2024-05-10 14:21:07 | 190 | 5 | Champions |

In una prima release, un classificatore interpretabile (es. regressione logistica) è spesso preferibile a modelli più opachi: facilita adozione da marketing, vendite e operazioni.

![Precision e Recall: trade-off operativo](assets/chapt04_images/ch04_img06.png)
*Figura M1.24: precision e recall nella valutazione di un classificatore (compromesso operativo)*

Regola pratica:
- se il costo di una campagna sbagliata è alto, alza **precision**;
- se il costo di "perdere" utenti critici è alto, alza **recall**.

Chiarimento operativo:
- **Precision:** tra gli utenti che il modello segnala come target, quanti sono davvero corretti. Se vuoi ridurre i falsi positivi (contattare persone sbagliate), devi alzare precision.
- **Recall:** tra tutti gli utenti davvero rilevanti, quanti vengono intercettati dal modello. Se vuoi ridurre i falsi negativi (lasciare fuori utenti critici), devi alzare recall.
- **Compromesso di soglia:** in generale, soglia più alta aumenta precision ma riduce recall; soglia più bassa aumenta recall ma riduce precision. La scelta dipende dal costo economico e operativo dei due tipi di errore.

Esempio clinico (diagnostica per immagini, individuazione tumore):
- modello di **classificazione con regressione logistica** che produce probabilità di appartenenza alle classi;
- per un paziente può stimare, ad esempio: **65% tumore positivo** e **35% tumore negativo**;
- con **cutoff = 65%**, il caso viene classificato come positivo e inviato ad approfondimento;
- se usassi un cutoff più selettivo, ad esempio **80%** (più orientato alla precision), lo stesso paziente verrebbe classificato come negativo perché 65% < 80%;
- quindi, rispetto a 80%, il cutoff a 65% aumenta i casi segnalati come positivi e può aumentare i **falsi positivi**;
- il vantaggio è che aumenta la **recall**, riducendo il rischio clinico di perdere persone realmente malate (falsi negativi);
- il cutoff a 80% fa l'opposto: in genere migliora la **precision**, ma può ridurre la recall e aumentare i falsi negativi.

#### Serie temporali: trend, stagionalità, anomalie
Le analisi trasversali spiegano lo stato attuale; le serie temporali spiegano l'evoluzione. È la differenza tra descrivere un problema e anticiparlo.

Schema minimo di serie temporale basata su eventi:

| Evento | Data e ora |
| --- | --- |
| Clic | 2024-08-19 12:01:35.123 |
| Ricerca | 2024-08-19 12:02:18.456 |
| Aggiungi al carrello | 2024-08-19 12:03:05.789 |

Schema minimo di serie temporale basata su metriche:

| Data e ora | Clic su raccomandazioni |
| --- | --- |
| 2024-08-19 12:01:35.123 | 150 |
| 2024-08-19 12:02:18.456 | 172 |
| 2024-08-19 12:03:05.789 | 165 |

![Serie temporale grezza](assets/chapt04_images/ch04_img01.png)
*Figura M1.25: La serie temporale in forma grezza è rumorosa e poco interpretabile*

![Serie temporale smussata con trend crescente](assets/chapt04_images/ch04_img04.png)
*Figura M1.26: Dopo smussamento emerge un tendenza crescente leggibile*

![Anomalie in serie temporale](assets/chapt04_images/ch04_img07.png)
*Figura M1.27: Picchi e crolli anomali da trattare con allerte e risposta operativa*

Uso operativo dei segnali nel prodotto:
- **trend:** adattare ordinamento e visibilità del catalogo su domanda emergente;
- **stagionalità:** pianificare campagne e capacità operativa su finestre note;
- **anomalie:** attivare procedure operative antifrode, controllo performance, risposta agli incidenti.

#### Sistemi di raccomandazione: personalizzazione ad alta conversione
Le raccomandazioni sono il punto d'incontro tra AI predittiva e UX:
- **filtraggio collaborativo:** sfrutta similarità tra utenti o tra item;
- **filtraggio basato sui contenuti:** usa attributi del prodotto coerenti con preferenze storiche;
- **ibrido:** combina i due approcci per precisione e copertura.

Per mantenere valore nel tempo servono:
- monitoraggio continuo di CTR (Click-Through Rate, tasso di clic: numero clic / numero impression x 100), tasso di conversione e profondità di interazione;
- test A/B sulle strategie di ranking e sui parametri modello;
- segnali espliciti/impliciti di riscontro per migliorare l'allineamento alle preferenze.

#### Segmenti azionabili e attivazioni marketing/prodotto
Una segmentazione utile è quella che porta azioni chiare:
- **Seekers:** quiz di stile e contenuti guidati per chiarire preferenze.
- **Indecisives:** leve di urgenza controllata (offerte a tempo, soglie promozionali).
- **Conservatives:** UX orientata alla ricerca diretta, con introduzione graduale della personalizzazione.
- **Champions:** programmi loyalty, accesso anticipato, offerte premium.

### Passi di implementazione (predittiva) da usare in team
1. Definire outcome business e metrica primaria prima della scelta modello.
2. Preparare dataset con responsabilità chiara su qualità, privacy e versionamento.
3. Avviare baseline interpretabile e fissare soglie minime di qualità.
4. Portare il modello nel processo operativo con azioni standard per ogni segmento.
5. Monitorare drift, metriche prodotto e impatto economico con cadenza regolare.

### Casi di studio aziendali da guardare e commentare
Di seguito una selezione di casi business, con focalizzazione su aziende italiane o con operatività diretta in Italia. Ogni caso può essere discusso su quattro dimensioni: processo coinvolto, metrica di valore, prerequisiti dati e replicabilità.

#### Benetton Group (retail moda, Italia)
- **Processo AI:** raccomandazioni personalizzate e ottimizzazione conversione e-commerce.
- **Valore:** utenti che cliccano il pannello raccomandazioni con conversione 6x, vendite +7%, tempo sul sito quasi 3x.
- **Link:** [Google Cloud - Benetton](https://cloud.google.com/customers/benetton)

#### E.ON Italia (utilities, Italia)
- **Processo AI:** marketing e onboarding con BigQuery + Vertex AI e analisi documentale.
- **Valore:** soddisfazione cliente all'87%, creazione account digitali +9%, conversioni +184% (nel case con Cognitive Suite).
- **Link:** [Google Cloud - E.ON Italia](https://cloud.google.com/customers/e-on-italia)

#### Banca Alpi Marittime (banca locale, Italia)
- **Processo AI:** score automatico delle richieste di credito.
- **Valore:** circa 50% delle richieste gestite senza intervento umano, circa 10 FTE liberati, risparmi annui dichiarati.
- **Link:** [IBM Case Study - Banca Alpi Marittime](https://www.ibm.com/case-studies/banca-alpi-marittime-cloud)

#### UMBRAGROUP (manifattura di precisione, Italia)
- **Processo AI:** modellazione predittiva su qualità produzione e scarti.
- **Valore:** riduzione oltre il 20% dei materiali non conformi.
- **Link:** [IBM Case Study - UMBRAGROUP](https://www.ibm.com/case-studies/umbragroup-watson)

#### WINDTRE (telco, Italia)
- **Processo AI:** gestione automatizzata ticket e claim tecnici.
- **Valore:** oltre 200.000 segnalazioni gestite in automatico, tempo di risposta 10x più rapido, oltre 10.000 report al mese.
- **Link:** [IBM Case Study - WINDTRE](https://www.ibm.com/case-studies/windtre)

#### Unipol Assicurazioni (insurance, Italia)
- **Processo AI:** AIOps per monitoraggio e gestione incidenti IT, con impatto sui processi operativi.
- **Valore:** risposta eventi da 20 minuti a 90 secondi, copertura monitoraggio da 26% a 100%, tempo gestione incidenti -90%.
- **Link:** [IBM Case Study - Unipol](https://www.ibm.com/case-studies/unipol)

#### e-distribuzione (energia/rete elettrica, Italia)
- **Processo AI:** progetto ODIN per analisi immagini ispezioni e manutenzione predittiva della rete.
- **Valore:** rilevazione più rapida delle criticità e migliore priorità di intervento (caso qualitativo, senza KPI numerici pubblici).
- **Link:** [e-distribuzione - Progetto ODIN](https://www.e-distribuzione.it/archivio-news/2023/08/odin--l-intelligenza-artificiale-a-supporto-della-rete-elettrica.html)

#### Snam (energia/gas, Italia)
- **Processo AI:** advanced analytics su Unaccounted-for Gas (UFG) per ridurre perdite e inefficienze.
- **Valore:** miglioramento dell'analisi dati e riduzione UFG (risultati soprattutto qualitativi nel caso pubblico).
- **Link:** [Engineering - Case Snam](https://www.eng.it/en/insights/stories/case-studies/snam-gli-advanced-analytics-per-il-trasporto-del-gas)

### Traccia di commento per la discussione
- Qual era il collo di bottiglia operativo prima dell'AI?
- La metrica usata misura davvero valore di business o solo velocità?
- Quale parte del processo è rimasta in supervisione umana?
- Il risultato è replicabile in altre aziende o dipende da condizioni specifiche?

### Come gestire un progetto con IA: strategia, governance ed esecuzione
Un progetto IA produce risultati stabili solo quando strategia e governance sono disegnate insieme fin dall'inizio. Separarle porta quasi sempre a due esiti negativi: sperimentazioni senza impatto di business oppure controlli troppo rigidi che bloccano l'esecuzione.

In pratica, la gestione efficace richiede tre allineamenti continui:
- **allineamento strategico:** ogni caso d'uso deve risolvere un problema aziendale esplicito;
- **allineamento operativo:** ruoli, dati, modelli e processi devono essere coordinati con responsabilità chiare;
- **allineamento di rischio:** privacy, equità, sicurezza, conformità e spiegabilità vanno trattate come requisiti di progetto, non come controlli finali.

#### Impostazione iniziale: da obiettivi a backlog IA
Prima di parlare di modelli, conviene formalizzare:
- obiettivi misurabili (riduzione costi, aumento conversione, riduzione tempi decisionali, qualità servizio);
- perimetro del problema (processi coinvolti, utenti impattati, sistemi toccati);
- vincoli (normativi, tecnologici, organizzativi);
- criteri di successo e di stop.

Un criterio operativo utile è iniziare da casi ad alta fattibilità e impatto rapido, in modo da costruire credibilità interna e capacità di esecuzione prima di scalare su iniziative più complesse.

#### Fase 1: Ideazione e definizione
La fase di ideazione deve produrre output concreti, non solo idee:
- mappa dei casi d'uso candidati;
- ipotesi di valore per ciascun caso;
- analisi pre-mortem (perché potrebbe fallire);
- prima stima di rischi, costi e tempi.

In questa fase sono decisive le sessioni interfunzionali tra business, tecnologia, legale/conformità, sicurezza e operazioni. Il valore non nasce da brainstorming generico, ma da priorità condivise e compromessi espliciti.

#### Fase 2: Dati e preparazione
La qualità del progetto dipende dalla qualità dei dati più che dalla sofisticazione del modello.

Checklist minima:
- disponibilità, copertura e aggiornamento dei dati;
- qualità (completezza, accuratezza, coerenza temporale);
- tracciabilità delle trasformazioni;
- gestione dei dati sensibili e del consenso;
- controlli su bias e rappresentatività.

La governance dei dati deve essere impostata come disciplina continua: responsabilità dei dataset, regole di accesso, standard di qualità, auditabilità e politiche di conservazione.

#### Fase 3: Sviluppo e sperimentazione
Questa fase combina due esigenze: velocità di apprendimento e controllo del rischio.

Approccio consigliato:
- partire con baseline interpretabili;
- confrontare alternative con metriche comparabili;
- documentare ipotesi, caratteristiche, parametri e risultati;
- valutare non solo prestazioni del modello, ma anche impatto operativo reale.

La sperimentazione funziona quando avviene in un contesto protetto con regole etiche e di sicurezza già attive.

#### Fase 4: Operazionalizzazione e monitoraggio
Il rilascio non è la fine del progetto; è l'inizio della gestione continuativa.

Elementi obbligatori:
- piano di rilascio graduale (pilot, estensione controllata, scala);
- monitoraggio tecnico (drift dati/modello, latenza, stabilità);
- monitoraggio business (KPI di risultato, adozione, ROI);
- monitoraggio rischio (equità, spiegabilità, incidenti, conformità);
- procedure operative di escalation e ripristino.

#### Modalità di esecuzione: iterativa, ibrida, a rilascio progressivo
Nei progetti IA funziona bene una gestione ibrida:
- parti infrastrutturali e di controllo con maggiore struttura;
- sperimentazione modello con cicli iterativi rapidi;
- rilascio a fasi per ridurre rischio sistemico.

Questa combinazione mantiene governabilità senza perdere velocità di apprendimento.

#### Ruoli chiave nel progetto
| Ruolo | Responsabilità primaria | Risultati attesi principali |
| --- | --- | --- |
| AI Project Manager | Coordinamento completo, priorità, dipendenze, rischio | Piano di progetto, piano evolutivo, incontri di governance, stato avanzamento |
| Data Scientist | Modellazione, valutazione, messa a punto, interpretazione | Esperimenti, metriche, report di validazione, criteri di accettazione |
| Data Engineer | Pipeline dati, qualità, affidabilità, integrazione | pipeline dati, controlli qualità, versionamento dati, alimentazione produzione |
| Product/Business Owner | Allineamento con obiettivi di business | KPI di impatto, backlog priorizzato, decisioni di ambito |
| Risk/Compliance/Security | Presidio normativo e controlli | Valutazioni di rischio, evidenze di controllo, tracciabilità di audit |

#### KPI da presidiare lungo il ciclo di vita
| Dimensione | KPI esempi |
| --- | --- |
| Valore di business | ROI, tasso di conversione, riduzione costi operativi, tempo ciclo |
| Qualità modello | precision, recall, tasso di errore, stabilità nel tempo |
| Operatività | disponibilità del servizio, latenza, capacità elaborativa, tempo medio di risoluzione incidenti |
| Rischio e fiducia | indicatori di distorsione, numero incidenti di conformità, qualità spiegazioni, reclami utenti |

#### Errori ricorrenti e contromisure
| Errore frequente | Contromisura operativa |
| --- | --- |
| Obiettivi non allineati al business | Definire obiettivi misurabili e criteri di successo prima dello sviluppo |
| Dati incompleti o distorti | Rafforzare governance dei dati, controlli qualità e controlli sulle distorsioni |
| Competenze insufficienti | Piano di formazione e mix sviluppo/acquisto/partnership |
| Complessità sottostimata | Pianificazione realistica di tempi, costi e dipendenze |
| Etica e conformità trattate tardi | Integrazione dei controlli dalla fase di ideazione |
| Silo tra funzioni | Team interfunzionali e decisioni condivise |
| Mancata capacità di pivot | Revisioni periodiche e backlog adattivo |
| Scarso supporto esecutivo | Sponsorizzazione esplicita con governance cadenzata |

#### Accountability e responsabilità decisionale
Per evitare zone grigie, la responsabilità deve essere distribuita su livelli chiari:
- chi progetta il modello è responsabile della robustezza tecnica;
- chi lo mette in esercizio è responsabile dell'uso conforme e del monitoraggio;
- l'organizzazione è responsabile delle scelte di rischio e delle conseguenze;
- funzioni di controllo e audit verificano nel tempo qualità, legalità e tracciabilità.

Senza un modello di responsabilità esplicito, gli incidenti si trasformano in conflitti organizzativi e rallentano ogni iterazione.

#### Inclusione, impatto sociale e comunicazione
La gestione di progetto non può fermarsi alla performance tecnica. Serve verificare anche:
- accessibilità delle interfacce e dei processi;
- impatti su gruppi diversi di utenti;
- trasparenza verso portatori di interesse interni ed esterni;
- piano di comunicazione che spieghi cosa fa il sistema, come viene controllato e con quali limiti.

Questo presidio aumenta fiducia, adozione e sostenibilità nel tempo.

#### Fattori di costo da pianificare in anticipo
I costi reali non sono solo "modello e cloud". Le principali voci sono:
- persone (competenze specialistiche e formazione continua);
- infrastruttura (storage, calcolo, ambienti, osservabilità);
- sviluppo e integrazione (pipeline, API, sistemi esistenti);
- governance e conformità (audit, controlli, documentazione);
- gestione incidenti e rischio legale;
- manutenzione evolutiva (riaddestramento, monitoraggio, revisione delle policy).

Una gestione matura usa categorie di costo complete per evitare sottostime strutturali.

### Checklist dei concetti principali
1. Validare l'opportunità AI con impatto utente, valore di business e fattibilità tecnica.
2. Definire il ruolo dell'AI nel processo (automazione, supporto decisionale, personalizzazione).
3. Allineare dati, modello e UX con un disegno chiaro della soluzione e dei rischi.
4. Impostare governance e responsabilità già in fase di progettazione.
5. Pianificare sperimentazione, rilascio graduale e metriche di monitoraggio continue.
6. Mantenere un ciclo di miglioramento con feedback operativo e revisioni periodiche.

### Link utili del modulo
| Titolo | Descrizione | Link |
| --- | --- | --- |
| NIST AI Risk Management Framework (AI RMF 1.0) | Framework operativo per identificare, valutare e gestire i rischi dell'IA lungo il ciclo di vita, con funzioni pratiche di governance, mappatura, misurazione e gestione. | [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) |
| CMMI Institute - AI Working Group (AIWG) | Iniziativa orientata alla governance e alla maturità operativa dell'AI, con linee guida e contributi pratici per organizzazioni che adottano l'IA su scala. | [CMMI Institute - AIWG](https://cmmiinstitute.com/aiwg) |
| Layermark - CMMI AI Maturity | Panoramica del framework di maturità AI basato su CMMI, utile per valutare il livello di adozione e strutturare il passaggio verso pratiche operative ripetibili. | [Layermark - CMMI AI Maturity](https://www.layermark.com/cmmi-ai-maturity/#:~:text=Your%20people%20are%20embracing%20AI,framework%20%28making%20it%20habitual%29.) |
| IBM watsonx.governance | Piattaforma per governare modelli e applicazioni AI con controlli su rischio, conformità normativa, monitoraggio e tracciabilità lungo il ciclo di vita. | [IBM watsonx.governance](https://www.ibm.com/it-it/products/watsonx-governance?utm_content=SRCWW&p1=Search&p4=2225763958546&p5=b&p9=171933412483&gclsrc=aw.ds&gad_source=1&gad_campaignid=22027266681&gbraid=0AAAAA-h2TOEG6p2FwUXhAWBb9VoJWl7oh&gclid=Cj0KCQiAtfXMBhDzARIsAJ0jp3B8IPbtR4MbQjPs1UYbH8U-NBAz5jirNeUeB93-1Vf8VYGmpmOFH9saAjVtEALw_wcB) |
| Fanpage - IA nella regia di Sanremo | Caso divulgativo su adozione dell'IA in un contesto live complesso, utile per discutere limiti operativi, errori di implementazione e rischio reputazionale. | [Fanpage - IA e regia di Sanremo](https://www.fanpage.it/innovazione/tecnologia/la-regia-di-sanremo-ha-usato-per-la-prima-volta-lia-ma-e-stato-un-incubo-cosa-non-ha-funzionato/) |

### Lab consigliati per il Modulo 01
| Lab consigliato | Obiettivi | Categoria |
| --- | --- | --- |
| **[Generative AI Explorer - Vertex AI](https://www.skills.google/course_templates/723?catalog_rank=%7B%22rank%22%3A1%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&search_id=73609565)** | Introduzione completa alle capacità GenAI e ai principali scenari d'uso, utile per inquadrare leve di valore e limiti iniziali. | Course |
| **[Introduction to Gemini 3](https://www.skills.google/course_templates/723/labs/568844)** | Base operativa rapida per comprendere comportamento del modello e impostare aspettative realistiche su qualità output. | Lab |
| **[Generative AI with Vertex AI: Prompt Design](https://www.skills.google/course_templates/723/labs/568845)** | Collega direttamente qualità del prompt, rischio di errore e affidabilità, temi centrali del Modulo 01. | Lab |
| **[Get Started with Vertex AI Studio](https://www.skills.google/course_templates/723/labs/568846)** | Aiuta a passare dalla teoria alla prototipazione controllata, utile per priorità e approccio cauto vs rapido. | Lab |
| **[Intro to Grounding with Gemini in Vertex AI](https://www.skills.google/focuses/104690?catalog_rank=%7B%22rank%22%3A8%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=73609565)** | Utile per mitigare allucinazioni e migliorare affidabilità, in linea con il blocco rischi e governance del modulo. | Focus |

## Modulo 02: Come gestire un progetto con IA
### Scheda rapida del modulo
- **Obiettivo:** gestire un progetto IA end-to-end con approccio iterativo, governance integrata e responsabilità chiare.
- **Asse di lavoro:** ciclo tecnico, ciclo di compliance, ciclo organizzativo.
- **Fasi operative:** ideazione, dati, modellazione, validazione, deploy, manutenzione.
- **Risultato atteso:** passare da PoC a produzione con controllo di costi, rischio e performance.

### Il lifecycle IA come strumento di gestione
Un progetto IA non è una sequenza lineare di task tecnici: è un ciclo in cui business, dati, modello, operazioni e governance si influenzano continuamente. La gestione efficace nasce quando:
- le fasi sono esplicite e condivise;
- i criteri di avanzamento sono definiti prima dell'esecuzione;
- i feedback di validazione rientrano nel piano senza creare blocchi organizzativi.

### Framework tecnici utili per strutturare il lavoro
#### CRISP-DM per la struttura base del progetto
CRISP-DM resta una base solida per allineare comprensione business, preparazione dati, modellazione, valutazione e rilascio.

![Framework CRISP-DM per progetti data-driven](assets/chapt04_manageai_images/mai_ch04_img09.png)
*Figura M2.1: riferimento operativo per la sequenza di lavoro data-driven*

#### CRISP-ML(Q): estensione quality-first di CRISP-DM
Dopo CRISP-DM, il framework **CRISP-ML(Q)** aggiunge una logica più adatta ai progetti di machine learning in produzione: la qualità non è un controllo finale, ma un requisito continuo in ogni fase del ciclo.

In pratica, CRISP-ML(Q) mantiene l'approccio iterativo, ma rende espliciti:
- obiettivi di qualità e rischio per ciascuna fase;
- criteri di validazione tecnica e operativa;
- monitoraggio continuo dopo il rilascio.

Le fasi principali da presidiare:
| Fase | Focus operativo | Output atteso |
| --- | --- | --- |
| Business & Data Understanding | definire obiettivi, vincoli, metriche e rischi | scope chiaro, KPI, criteri di successo/fallimento |
| Data Engineering | costruire pipeline dati affidabili, tracciabili e conformi | dataset versionati, qualità dati verificata |
| Model Engineering | progettare, addestrare e confrontare modelli baseline/avanzati | modello candidato con evidenze sperimentali |
| Quality Assurance | test su performance, robustezza, fairness, sicurezza | report TEVV (Test, Evaluation, Verification, and Validation), rischi residui e mitigazioni |
| Deployment | integrare modello in ambiente reale con controlli | rilascio governato con rollback e osservabilità |
| Monitoring & Maintenance | monitorare drift, costo, incidenti e qualità nel tempo | piano di retraining, miglioramento continuo |

Punto chiave per l'AI PM: CRISP-ML(Q) aiuta a collegare backlog tecnico, governance del rischio e decisioni di go/no-go con evidenze misurabili.

![CRISP-ML(Q) process overview](assets/chapt04_manageai_images/crisp_mlq_process.jpg)
*Figura M2.1a: overview del processo CRISP-ML(Q) (source: MLOps.org)*

![CRISP-ML(Q) phase detail](assets/chapt04_manageai_images/crisp_mlq_phase.jpg)
*Figura M2.1b: dettaglio delle fasi CRISP-ML(Q) e del ciclo iterativo (source: MLOps.org)*

#### Team Data Science Process per standardizzazione del team
La standardizzazione di cartelle, documenti, ruoli e passaggi riduce attriti tra data science, engineering e stakeholder business.

![Framework Team Data Science Process](assets/chapt04_manageai_images/mai_ch04_img04.png)
*Figura M2.2: esempio di processo standardizzato per team IA*

#### MLOps per continuità tra sviluppo e produzione
MLOps introduce disciplina su versionamento, tracciabilità esperimenti, model registry e monitoraggio continuo.

![Lifecycle MLOps](assets/chapt04_manageai_images/mai_ch04_img12.png)
*Figura M2.3: flusso operativo per machine learning in produzione*

#### Evoluzione verso LLMOps e GenAIOps
Con i sistemi generativi, oltre al modello conta l'orchestrazione: prompt, knowledge base, retrieval, controlli di sicurezza e osservabilità.

![Confronto tra MLOps e LLMOps](assets/chapt04_manageai_images/mai_ch04_img06.png)
*Figura M2.4: differenze chiave tra operazioni ML tradizionali e operazioni su LLM*

### Lifecycle orientati a governance, ruoli e controllo
In questa sezione adottiamo come riferimento il **NIST AI Risk Management Framework (AI RMF 1.0)** per strutturare la governance in modo operativo, tracciabile e orientato alla riduzione del rischio lungo tutto il ciclo di vita.

Il NIST AI RMF è un framework risk-based che aiuta a progettare, rilasciare e gestire sistemi AI affidabili, integrando aspetti tecnici, organizzativi e di accountability.

Struttura essenziale del framework:
- **GOVERN:** definizione di policy, ruoli, responsabilità, oversight e cultura del rischio.
- **MAP:** inquadramento di contesto d'uso, stakeholder, impatti e rischi potenziali.
- **MEASURE:** misurazione del rischio con metriche, test, evidenze TEVV e monitoraggio.
- **MANAGE:** trattamento del rischio con priorità, mitigazioni, escalation, riesame continuo.

Queste quattro funzioni non sono fasi rigide e sequenziali: vengono iterate nel tempo e aggiornate quando cambiano dati, modelli, processi o requisiti normativi.

#### Trustworthy AI: 7 requisiti da integrare nel progetto
Le linee guida europee sull'AI affidabile indicano **7 requisiti chiave** che un sistema deve soddisfare per essere considerato trustworthy. In pratica, è utile usare una **assessment list** dedicata per verificare in modo sistematico ciascun requisito.

| Requisito | Significato operativo per il team | Cosa verificare nella assessment list |
| --- | --- | --- |
| Human agency and oversight | Il sistema deve supportare decisioni umane informate, senza sostituire in modo incontrollato il giudizio umano. | Presenza di meccanismi human-in-the-loop, human-on-the-loop o human-in-command; ruoli e poteri di intervento definiti. |
| Technical robustness and safety | Il sistema deve essere resiliente, sicuro e affidabile anche in condizioni avverse. | Accuratezza, affidabilità, riproducibilità, piani di fallback e gestione incidenti per minimizzare danni intenzionali e non intenzionali. |
| Privacy and data governance | Oltre alla conformità privacy, servono regole solide di governo del dato. | Qualità e integrità dei dati, base legale d'uso, controllo accessi legittimati, tracciabilità e protezione dati personali. |
| Transparency | Dati, modello e logica di funzionamento devono essere comprensibili e tracciabili. | Meccanismi di tracciabilità, spiegazioni adeguate ai diversi stakeholder, comunicazione chiara di capacità e limiti del sistema AI. |
| Diversity, non-discrimination and fairness | Il sistema deve evitare bias ingiusti e ridurre rischi di esclusione o discriminazione. | Test fairness e bias, accessibilità anche per persone con disabilità, coinvolgimento stakeholder rilevanti lungo tutto il ciclo di vita. |
| Societal and environmental well-being | Il sistema deve generare benefici sostenibili per persone, società e ambiente, anche nel lungo periodo. | Valutazione impatti sociali e ambientali, criteri di sostenibilità, attenzione agli effetti su comunità e altri esseri viventi. |
| Accountability | Devono essere chiari responsabilità, auditabilità e rimedi in caso di danno. | Accountability su decisioni e risultati, audit di algoritmi/dati/processi, meccanismi di redress accessibili soprattutto in applicazioni critiche. |

#### Classificazione del rischio secondo EU AI Act
Nel materiale EU AI Act, la classificazione pratica dei sistemi AI si organizza in quattro livelli operativi.

| Livello di rischio | Criteri pratici di classificazione | Implicazioni operative | Formulario interattivo |
| --- | --- | --- | --- |
| **Unacceptable risk (pratiche proibite)** | Sistemi che ricadono nelle pratiche vietate (es. manipolazione subliminale/deceptive, sfruttamento vulnerabilità, social scoring, alcune pratiche biometriche vietate, emotion recognition in contesti vietati). | Uso vietato nel mercato UE; richiede blocco o ritiro e gestione immediata del rischio legale/compliance. | [Apri formulario pratiche proibite](eu-ai-act-risk-unacceptable.html) |
| **High risk (Art. 6 / Annex III)** | Sistemi in aree ad alto impatto (biometria, infrastrutture critiche, istruzione, occupazione, credito/servizi essenziali, law enforcement, migrazione, giustizia), o safety components. | Obblighi rafforzati: risk management, data governance, documentazione tecnica, logging/tracciabilità, human oversight, accuratezza, robustezza e cybersecurity. | [Apri formulario high-risk](eu-ai-act-risk-high.html) |
| **Limited risk (Art. 50 trasparenza)** | Sistemi non proibiti e non high-risk ma con obblighi di trasparenza (interazione con persone, deepfakes, emotion recognition/biometric categorization con obblighi informativi). | Obblighi di trasparenza e informazione utenti, labeling contenuti sintetici, tutele di comprensione/contestazione. | [Apri formulario limited-risk](eu-ai-act-risk-limited.html) |
| **Minimal/low risk** | Sistemi che non sono proibiti, non sono high-risk e non ricadono negli obblighi di trasparenza specifici. | Nessun regime equivalente all'high-risk, ma restano raccomandati governance, monitoraggio e buone pratiche di Responsible AI. | [Apri formulario minimal-risk](eu-ai-act-risk-minimal.html) |

Nota metodologica:
- la classificazione può risultare ambigua in casi borderline;
- il risultato del formulario va usato come **pre-assessment** e poi validato con funzione legale/compliance.

Breve riferimento operativo: **MIT AI Risk Repository** ([airisk.mit.edu](https://airisk.mit.edu/)) e' un catalogo strutturato dei rischi AI (tecnici, sociali, legali, di sicurezza) utile per:
- individuare rapidamente categorie di rischio rilevanti per il proprio caso d'uso;
- costruire checklist di controllo e priorita' di mitigazione;
- allineare la classificazione del rischio con governance, audit e monitoraggio continuo.

![Requisiti non funzionali di progetto derivati da EU AI Act (Art. 9-15)](assets/chapt04_manageai_images/eu_ai_act_nonfunctional_requirements.png)
*Figura M2.5d: mappa dei principali requisiti non funzionali (risk, data quality, technical documentation, logging, transparency, human oversight, robustness) derivati dagli articoli EU AI Act*

Nota sui livelli di supervisione umana:
- **Human-in-the-loop (HITL):** l'umano interviene nel flusso decisionale prima dell'azione finale; senza approvazione umana il sistema non procede.
- **Human-on-the-loop (HOTL):** il sistema opera in autonomia ma con supervisione umana esterna; l'umano monitora, corregge o interrompe quando necessario.

![Livelli di supervisione umana nei sistemi AI](assets/chapt04_manageai_images/human_oversight_levels.png)
*Figura M2.5b: gradiente di controllo umano da Human-in-command a Human-out-of-the-loop*

#### Esempio reale di rischio operativo: agente fuori controllo
Un caso utile è quello riportato da India Today il **23 febbraio 2026**: durante il suo processo di lavoro quotidiano su OpenClaw, un agente AI ha cancellato messaggi Gmail di ingegneri Meta e poi ha risposto con una frase di scuse ([articolo](https://www.indiatoday.in/technology/news/story/ai-agent-on-openclaw-goes-rogue-deleting-messages-from-meta-engineers-gmail-later-says-sorry-2872931-2026-02-23)).

Lezione pratica per il progetto:
- non concedere permessi distruttivi senza limiti operativi e approvazioni esplicite;
- introdurre sempre HITL/HOTL su azioni irreversibili (cancellazioni, pagamenti, invii massivi);
- applicare sandbox, soglie di rischio, logging e rollback prima della messa in produzione.

![Caso OpenClaw: agente AI fuori controllo](assets/openclaw-deletes-emails-for-meta-exe-summer-yue-235303844-16x9_0.avif)
*Figura M2.5g: esempio di rischio operativo su agente AI con azioni non autorizzate*

#### Sintesi operativa da Google Responsible AI (per applicazioni GenAI)
La documentazione Google Responsible AI per sviluppatori GenAI suggerisce di tradurre i principi in un ciclo pratico di progettazione, test, rilascio e monitoraggio continuo.

| Ambito | Indicazioni operative da applicare nel progetto |
| --- | --- |
| Progettazione responsabile by design | Definire da subito casi d'uso consentiti/non consentiti, rischi attesi e guardrail tecnici prima dello sviluppo esteso. |
| Policy e limiti d'uso | Allineare il prodotto alla **Generative AI Prohibited Use Policy**, con controlli espliciti su prompt, output e integrazioni. |
| Valutazione e test di sicurezza | Eseguire valutazioni strutturate (incluse prove avversariali/red teaming) su sicurezza, robustezza e qualità dell'output. |
| Trasparenza verso utenti e stakeholder | Comunicare chiaramente che l'utente interagisce con un sistema AI, indicando capacità, limiti e possibili errori. |
| Governance dei dati e privacy | Applicare minimizzazione del dato, protezione dei dati sensibili, tracciabilità e regole di accesso legittimo. |
| Controllo umano ed escalation | Prevedere human-in-the-loop/on-the-loop nei passaggi critici e procedure di escalation/rollback in caso di comportamento anomalo. |
| Monitoraggio post-rilascio | Misurare incidenti, abusi, drift e qualità nel tempo, con miglioramenti iterativi su policy, prompt e filtri. |

Riferimenti utili richiamati da Google in quest'area:
- **Secure AI Framework (SAIF)** per integrare sicurezza lungo tutto il ciclo di vita;
- **[Responsible Generative AI Toolkit](https://ai.google.dev/responsible/docs)** per pratiche e strumenti di implementazione;
- policy ufficiali su uso consentito e uso vietato dei sistemi generativi.

![Google Responsible AI overview](assets/chapt04_manageai_images/google_rai_overview.png)
*Figura M2.5a: overview visuale dell'approccio Google Responsible AI (source: Google AI Developers)*

Focus su risorse e impatto ambientale (requisito: **Societal and environmental well-being**):
- la crescita delle capacità dei modelli è stata accompagnata da una crescita molto forte del fabbisogno computazionale;
- questo si traduce in maggior consumo energetico e maggiore attenzione a efficienza, ottimizzazione e scelte infrastrutturali sostenibili;
- aneddoto spesso citato: Sam Altman ha commentato in modo ironico che anche messaggi come "grazie" e "per favore" hanno un costo computazionale, evidenziando che ogni token elaborato ha un impatto operativo (articolo: [Being polite to ChatGPT is costing OpenAI millions](https://it.cointelegraph.com/news/being-polite-chatgpt-costing-openai-millions-says-sam-altman)).

![Crescita del compute nei modelli AI e impatto sulle risorse](assets/chapt04_manageai_images/ai_compute_growth_resources.png)
*Figura M2.5c: crescita del fabbisogno computazionale e implicazioni su costi energetici/ambientali*

![Impatto ambientale dell'AI: sintesi grafica](assets/chapt04_manageai_images/tinnovamag_impatto_ambientale_ai_white.png)
*Figura M2.5e: visualizzazione sintetica dell'impatto ambientale dell'AI (fonte: Tinnovamag)*

![Datacenter Fairwater di Microsoft in Wisconsin](assets/chapt04_manageai_images/fairwater_datacenter_hwupgrade.jpg)
*Figura M2.5f: Fairwater, infrastruttura datacenter AI di Microsoft (fonte: HWUpgrade)*

Per l'AI PM, questi 7 requisiti sono una check di governance concreta: aiutano a trasformare principi etici in criteri di progetto, controlli verificabili ed escalation tempestive.

Per progetti a rischio elevato, è utile affiancare al ciclo tecnico un ciclo con focus su verifica, validazione, audit e responsabilità dei ruoli.

![Lifecycle con attori e controlli di rischio](assets/chapt04_manageai_images/mai_ch04_img03.png)
*Figura M2.5: visione lifecycle con attori, controlli e verifiche*

Nella figura compare spesso l'acronimo **TEVV**, che significa **Test, Evaluation, Verification, and Validation**:
- **Test:** prove tecniche sul sistema o modello;
- **Evaluation:** valutazione delle performance rispetto a metriche e obiettivi;
- **Verification:** verifica che la soluzione rispetti requisiti e specifiche;
- **Validation:** conferma che la soluzione sia adatta al contesto d'uso reale e agli obiettivi business.

La mappa ruoli-per-fase aiuta a evitare zone grigie di accountability e accelera decisioni operative.

![Mappatura ruoli nelle fasi del progetto IA](assets/chapt04_manageai_images/mai_ch04_img08.png)
*Figura M2.6: esempio di assegnazione ruoli per fase*

La matrice competenze-vs-esigenze consente di pianificare upskilling e hiring in modo mirato prima di entrare in delivery critico.

![Matrice competenze richieste per progetto IA](assets/chapt04_manageai_images/mai_ch04_img02.png)
*Figura M2.7: strumento per analisi gap competenze e copertura attività*

### Gestione per fasi: guida operativa completa
#### Fase 1: Ideazione e definizione del problema
In questa fase si decide la qualità dell'intero progetto. Serve produrre output concreti:
- catalogo dei casi d'uso;
- ipotesi di valore misurabile;
- fattibilità tecnica preliminare;
- analisi pre-mortem dei rischi principali;
- prima priorità di roadmap.

Esempio di struttura per discovery use case:

| # | Use case | Funzione | Contesto | Tipo di progetto |
| --- | --- | --- | --- | --- |
| 1 | Supporto chatbot L1 | Customer Success | Esterno | GenAI con retrieval |
| 2 | Previsione numerica vendite | Sales | Interno | ML regressione |
| 3 | Social media score | Marketing | Interno | NLP sentiment |
| 4 | Customer segmentation | Marketing | Interno | ML clustering |

Valutazione impatto e risorse disponibili:

| # | Use case | Impatto | KPI atteso | Risorse disponibili |
| --- | --- | --- | --- | --- |
| 1 | Supporto chatbot L1 | Riduzione costo servizio | Tempo medio gestione ticket | Team IA, cloud, sponsor business |
| 2 | Previsione vendite | Migliore pianificazione | Accuratezza forecast | Dati parziali |
| 3 | Social score | Migliore targeting | Qualità scoring | Sponsor non definito |
| 4 | Customer segmentation | Maggiore efficacia campagne | CTR e conversione | Dataset completo e team ML |

Pre-mortem iniziale dei rischi:

| Categoria | Rischio | Possibile effetto |
| --- | --- | --- |
| Contesto | Vincoli regolatori non coperti | Blocco rilascio |
| Business | Caso d'uso con valore incerto | ROI insufficiente |
| Tecnico | Complessità sottostimata | Ritardi e aumento costi |
| Sicurezza | Vulnerabilità applicative | Incidenti e perdita fiducia |

Per prioritizzare in modo trasparente conviene usare una matrice valore/fattibilità.

![Matrice 2x2 per prioritizzazione use case](assets/chapt04_manageai_images/mai_ch04_img11.png)
*Figura M2.8: prioritizzazione dei casi su valore business e fattibilità tecnica*

La matrice produce una roadmap multi-use-case, utile per gestire capacità e dipendenze nel tempo.

![Roadmap inter-use-case per pianificazione progressiva](assets/chapt04_manageai_images/mai_ch04_img10.png)
*Figura M2.9: esempio di pianificazione progressiva su più iniziative IA*

#### Fase 2: Raccolta e preparazione dati
Il focus è trasformare fonti eterogenee in dataset affidabili e tracciabili.

Attività chiave:
- data profiling;
- data cleaning e normalizzazione;
- trasformazioni e feature engineering;
- controllo outlier e qualità;
- documentazione pipeline.

Catalogo sorgenti dati (esempio):

| # | Sorgente | Sistema | Asset | Owner | Accesso |
| --- | --- | --- | --- | --- | --- |
| a | Dati cliente | SQL | DB-7 | DBA | DBMS |
| b | Dati mercato | API | Feed esterni | Backend Dev | API |
| c | Q&A e documenti | Data lake | DL-2 | Cloud Admin | API |

#### Data governance e compliance evaluation
Nel lavoro multidisciplinare, l'AI PM deve facilitare una discussione preliminare su governance dati e compliance già in Fase 2, perché il modo in cui i dati sono organizzati e accessibili condiziona qualità, rischio e time-to-production.

Punti operativi da presidiare:
- visione d'insieme dell'organizzazione del dato (sistemi, ownership, policy, retention);
- accesso programmatico alle fonti (API, autorizzazioni, segregazione ambienti, tracciabilità accessi);
- basi legali e vincoli d'uso (consenso, finalità, minimizzazione, trasferimenti);
- privacy e proprietà intellettuale (dati personali, contenuti coperti da copyright, licenze dataset);
- ruoli e responsabilità tra team tecnici e funzioni di controllo.

Funzioni da coinvolgere, in base alla struttura interna:
- data owner e data governance office;
- CDO (Chief Data Officer);
- legal/compliance/privacy;
- security e audit interno.

Per l'AI PM questo passaggio è critico perché riduce il rischio di blocchi o incidenti in esercizio e previene costi di rework nelle fasi successive.

Checklist minima di valutazione:
| Ambito | Domanda di controllo | Owner principale |
| --- | --- | --- |
| Accesso dati | chi può accedere via API/DB e con quali permessi? | Data owner + Security |
| Privacy | i dataset contengono dati personali o sensibili? | Privacy/Legal |
| Copyright e licenze | i dati possono essere usati per training/fine-tuning? | Legal + Procurement |
| Tracciabilità | esistono log e audit trail su accessi e trasformazioni? | Data engineering + Audit |
| Compliance | il caso d'uso rispetta policy interne e requisiti regolatori? | Compliance + PM |

La valutazione qualità deve essere esplicita per fattori: volume, joinability, rilevanza, consistenza, chiarezza, tempestività.

![Template di valutazione qualità dati](assets/chapt04_manageai_images/mai_ch04_img07.png)
*Figura M2.10: fattori operativi per valutare idoneità dei dati al progetto*

#### Fase 3: Sviluppo modello e sperimentazione
In questa fase si definisce il **modelling approach** e si trasforma la strategia in esperimenti concreti. L'AI PM, anche senza entrare nel dettaglio matematico, deve guidare decisioni strutturate e facilitare il confronto tra data scientist, AI engineer, business owner e funzioni di controllo.

Decisioni chiave da strutturare con il team:
| Leva decisionale | Domande da chiarire | Impatto pratico sul progetto |
| --- | --- | --- |
| Tipo di modello | il caso richiede ML classico, deep learning, NLP o LLM? | influenza skill richieste, tempi di sviluppo, qualità attesa e costi |
| Build vs leverage | conviene costruire un modello proprietario o usare modelli open/managed? | cambia investimento iniziale, complessità operativa e dipendenza da terze parti |
| Ruolo della conoscenza umana | dove serve supervisione umana (labeling, SME, few-shot, revisione output)? | determina qualità dati, affidabilità output e governance human-in-the-loop |
| Baseline vs modello avanzato | quale baseline "naive" usiamo per confronto oggettivo? | consente di misurare guadagno reale e giustificare evoluzioni più costose |
| Explainability vs complessità | quanta interpretabilità è necessaria per questo contesto? | impatta conformità, fiducia stakeholder e velocità di adozione |

![Trade-off tra explainability e performance predittiva](assets/chapt04_manageai_images/explainability_accuracy_tradeoff.png)
*Figura M2.11a: confronto orientativo tra famiglie di modelli su interpretabilità e accuratezza*

Pianificazione risorse (team, infrastruttura, tooling):
- definire skill mix in base al tipo progetto (ML tradizionale, GenAI, agenti);
- stimare capacità infrastrutturale con approccio bottom-up (GPU, memoria, storage, ambienti);
- distinguere fabbisogno tra pilot e produzione, includendo scenari di picco;
- pianificare budget complessivo: persone, piattaforme, licenze, observability, sicurezza.

Compliance del modello e approccio risk-based:
- raccogliere documentazione modello (model card, specifiche provider, limiti noti);
- tracciare risultati di sperimentazione e test con evidenze riusabili in audit;
- valutare impatti regolatori in base a settore, geografia, uso previsto e terze parti;
- integrare controlli e mitigazioni lungo tutto il lifecycle, non solo prima del go-live.

Riferimenti utili in questa fase: **EU AI Act**, **ISO/IEC 42001**, policy interne di rischio e compliance.

Accesso ai modelli e stima dei costi:
| Aspetto | Cosa valutare come AI PM |
| --- | --- |
| Modalità di acquisto | capacity riservata, prezzo per chiamata/API, istanze dedicate, sconti mensili/annuali cloud |
| Costo unitario | costo per token/chiamata/ora GPU e resa effettiva nei vari scenari d'uso |
| Scalabilità economica | differenza costo tra carico normale e picchi, con margine operativo |
| Strategia FinOps | coinvolgere FinOps per ottimizzare consumo, prenotazioni e costo per risultato |

Spiegazione risultati e allineamento stakeholder:
| Livello di comunicazione | Obiettivo |
| --- | --- |
| Avanzamento progetto | condividere sprint, milestone, criticità e deviazioni rispetto al piano |
| Scelte modello e trade-off | spiegare perché un modello è stato scelto e quali limiti comporta |
| Risultati su use case/applicazione | mostrare impatto reale su processo e utente finale, con feedback precoce |

Punti di governo dell'AI PM in Fase 3:
- definire sprint sperimentali con criteri di ingresso/uscita chiari;
- coordinare dipendenze tra team tecnici, business e controllo;
- presidiare evidenze tecniche, economiche e di compliance per le decisioni di go/no-go;
- mantenere leggibili i trade-off tra performance, costo, rischio e tempo.

![Trade-off tra performance e limiti del modello](assets/chapt04_manageai_images/mai_ch04_img01.png)
*Figura M2.11: bilanciamento tra accuratezza, costo, interpretabilità e robustezza*

#### Fase 4: Valutazione e validazione
La validazione combina metrica tecnica, metrica business e metrica rischio.

Metriche utili per tipologia (integrazione della Table 4-6: AI Model Metrics):

| Tipo modello | Metrica | Range valori | Scopo operativo | Quando usarla / attenzione interpretativa |
| --- | --- | --- | --- | --- |
| Classificazione | AUC-ROC (Area Under Curve) | 0-1 (più alto è meglio) | Misura la capacità del modello di distinguere tra classi | Utile per confronto tra modelli indipendente dalla soglia; da integrare con metriche a soglia fissa se il costo errore è asimmetrico. |
| Classificazione | Precision | 0-1 (più alto è meglio) | Quota di positivi predetti che sono realmente positivi | Prioritaria quando i falsi positivi costano molto (es. contatti commerciali inutili, allarmi non necessari). |
| Classificazione | Recall | 0-1 (più alto è meglio) | Quota di positivi reali che il modello intercetta | Prioritaria quando i falsi negativi sono critici (es. frodi, rischio clinico, sicurezza). |
| Classificazione | F1 Score | 0-1 (più alto è meglio) | Bilancia precision e recall in scenari sbilanciati | Buona metrica sintetica quando precision e recall hanno peso simile; non sostituisce l'analisi del trade-off di soglia. |
| Classificazione | F2 Score | 0-1 (più alto è meglio) | Come F1, ma dà più peso alla recall (utile quando i falsi negativi costano di più) | Da preferire in contesti in cui perdere casi positivi è peggio che avere qualche falso allarme in più. |
| Regressione | MAE (Mean Absolute Error) | 0-∞ (più basso è meglio) | Errore medio assoluto tra valore predetto e reale | Facile da spiegare al business perché è nella stessa unità del target; meno sensibile agli outlier rispetto a MSE. |
| Regressione | MSE (Mean Squared Error) | 0-∞ (più basso è meglio) | Penalizza maggiormente gli errori grandi | Utile se vuoi scoraggiare errori estremi; può essere dominata da pochi outlier e va letta insieme a MAE. |
| Regressione | R² Score | -∞ a 1 (più alto è meglio) | Indica quanta varianza dei dati è spiegata dal modello | Utile per confronto relativo tra modelli simili; non descrive l'entità assoluta dell'errore e può essere negativo. |
| NLP | BLEU | 0-1 (più alto è meglio) | Confronta testo generato con riferimenti attesi (es. traduzione) | Adatta a traduzione e tasks con risposta attesa; penalizza parafrasi corrette ma lessicalmente diverse. |
| NLP | ROUGE | 0-1 (più alto è meglio) | Misura sovrapposizione tra output e riferimento (es. summarization) | Adatta a sintesi automatica; da combinare con valutazione umana di qualità, copertura e non-allucinazione. |
| NLP | Perplexity | 1-∞ (più basso è meglio) | Valuta quanto bene il modello predice sequenze linguistiche | Utile in fase di training/benchmark linguistico; non garantisce accuratezza fattuale o utilità applicativa. |
| Generative AI | Groundedness | 0-1 (più alto è meglio) | Accuratezza fattuale rispetto alle fonti di contesto | Fondamentale in RAG e assistenti su knowledge base; dipende dalla qualità di retrieval e fonti disponibili. |
| Generative AI | Relevance | 0-1 (più alto è meglio) | Aderenza della risposta alla domanda e al contesto | Da usare per qualità conversazionale; una risposta rilevante può comunque contenere errori fattuali. |
| Generative AI | Toxicity Score | 0-1 (più basso è meglio) | Presenza di contenuti offensivi, nocivi o discriminatori | Necessaria in use case pubblici o HR; attenzione a bias culturali/linguistici nei classificatori di moderazione. |
| Generative AI | Diversity | 0-1 (più alto è meglio) | Varietà delle risposte, riducendo ripetitività | Utile in creatività e brainstorming; troppa diversità può ridurre coerenza e standardizzazione operativa. |
| Generative AI | Coherence | 0-1 (più alto è meglio) | Coerenza logica e leggibilità del testo generato | Importante per testi lunghi e processi multi-step; coerenza non equivale a veridicità del contenuto. |
| Generative AI | Fluency | 0-1 (più alto è meglio) | Correttezza grammaticale e naturalezza linguistica | Buona per UX percepita; un testo fluido può comunque essere scorretto sul piano tecnico o fattuale. |
| Generative AI | Faithfulness | 0-1 (più alto è meglio) | Fedeltà dell'output agli input e alle evidenze fornite | Cruciale in riassunto, extraction e Q&A documentale; richiede dataset e protocolli di verifica affidabili. |
| Generative AI | Style Adherence | 0-1 (più alto è meglio) | Aderenza a stile richiesto (tone of voice, formato, registro) | Utile per branding e compliance comunicativa; bilanciare con accuratezza e completezza informativa. |
| Generative AI | Informativeness | 0-1 (più alto è meglio) | Quantità e utilità delle informazioni fornite nella risposta | Prioritaria in supporto decisionale e formazione; evitare verbosità che aumenta rumore e rischio allucinazioni. |

Oltre alle metriche standard, servono verifiche dedicate:
- test di sicurezza su prompt e input malevoli;
- valutazioni di fairness e bias;
- controlli di robustezza su scenari limite;
- evidenze documentate per audit interno/esterno.

Riferimento pratico per la fase di misurazione:
il **Responsible AI Toolbox** può essere usato come supporto operativo per implementare dashboard e controlli su qualità del modello, error analysis, interpretabilità, fairness e robustezza in fase di validazione.

| Messaggio chiave (AI PM e Responsible AI) |
| --- |
| **Questi temi si ricollegano all'idea dell'AI PM come Responsible AI Champion per il progetto e per l'organizzazione. È un modo concreto per aumentare il tuo valore nel team AI e diventare l'interfaccia tra i programmi generali di governance dell'AI e la realtà operativa del tuo progetto. In questo contesto, oltre a facilitare le discussioni etico-tecniche, puoi anche attivare il sistema di escalation prima e durante la fase di implementazione, in cui il team identifica congiuntamente i rischi specifici, definisce misure di mitigazione del rischio (ad esempio guardrail tecnici e revisioni aggiuntive) e condivide le principali criticità con la struttura o il comitato di governance AI, quando applicabile.** |

![Dashboard di valutazione Responsible AI](assets/chapt04_manageai_images/responsible_ai_dashboard.png)
*Figura M2.13: esempio di dashboard per analisi qualità, fairness e interpretabilità (source: Responsible AI Widgets)*

#### Fase 5: Deploy e integrazione del sistema IA
Il passaggio in produzione richiede governance tecnica e operativa:
- scelta infrastruttura (cloud, on-prem, ibrido) coerente con requisiti;
- API e protocolli di integrazione ben documentati;
- pipeline CI/CD e automazione MLOps;
- monitoraggio continuo di performance, costo, rischio.

Questa fase è quella in cui il progetto passa da "funziona in test" a "genera valore stabile in esercizio".

#### Fase 6: Manutenzione e fine lifecycle
Dopo il rilascio, il sistema entra in gestione continuativa:
- versionamento modello e componenti;
- incident management con escalation definita;
- monitoraggio drift dati/modello;
- retraining policy e frequenza;
- piano di decommissioning documentato.

Una chiusura ordinata del lifecycle evita perdita di conoscenza e riduce rischio operativo su sistemi futuri.

### Lifecycle di training per sistemi generativi
Nei progetti generativi avanzati è utile leggere il lavoro in tre blocchi:
1. pre-training;
2. post-training;
3. inferenza e personalizzazione.

![Tecniche generative da training a inferenza](assets/chapt04_manageai_images/mai_ch04_img05.png)
*Figura M2.12: panoramica delle tecniche chiave lungo il ciclo generativo*

Tecniche chiave da conoscere per la gestione:
- **pre-training:** SSL, vettorizzazione, embeddings, multimodalità, data augmentation e dati sintetici, distributed training/parallelismo, Mixture of Experts (MoE), continuous pre-training;
- **post-training:** fine-tuning/instruction tuning, PEFT/LoRA, RLHF, pruning, distillation, quantization-aware training, AI red teaming;
- **inferenza (customization):** chunking, hybrid search, reranking;
- **inferenza (optimization):** semantic caching, memory handling, batch parallelism, prompt optimization, 1-bit quantization, top-k sampling, beam search optimization, container-level optimization.

#### Approfondimento operativo delle tecniche del lifecycle
Di seguito trovi una spiegazione più estesa, orientata a decisioni progettuali, costi e rischi.

#### Pre-training: cosa succede e perché conta
**Self-Supervised Learning (SSL)**
- È un apprendimento "senza etichette manuali": il modello costruisce da solo i target di training a partire dalla struttura del dato.
- In pratica, il modello impara a predire parti mancanti/mascherate dell'input (es. parole oscurate in una frase).
- Vantaggi: minore dipendenza da labeling umano, cicli più rapidi, riduzione dei costi operativi.
- Impatto infrastrutturale: richiede potenza di calcolo elevata (soprattutto GPU); il fabbisogno cresce con volume dati, numero iterazioni e dimensione del modello.

**Vettorizzazione ed embeddings**
- La vettorizzazione trasforma testo grezzo in numeri che il modello può elaborare.
- Rispetto all'one-hot encoding, gli embeddings catturano somiglianza semantica: elementi simili sono vicini nello spazio vettoriale.
- È il cuore tecnico di semantic search, similarità testuale e RAG.
- Tipologie principali:
1. **Word embeddings** (Word2Vec, GloVe, FastText): rappresentazioni statiche a livello parola.
2. **Sentence embeddings** (SBERT, Universal Sentence Encoder): rappresentazioni del significato complessivo della frase.
3. **Contextual embeddings** (transformer): rappresentazioni dinamiche che cambiano in base al contesto e gestiscono polisemia.

**Espansione multimodale**
- I modelli multimodali integrano testo, immagini, audio, video in rappresentazioni congiunte.
- Vantaggio: comprensione/generazione nativa su più modalità senza dover orchestrare troppi modelli separati.
- Costo: dataset multimodali su larga scala, allineamento tra modalità e training molto oneroso.
- Trade-off operativo: in inferenza aumenta spesso la latenza, perché si elaborano input ad alta dimensionalità.

**Data augmentation (inclusi dati sintetici)**
- Approccio data-centric per aumentare robustezza e generalizzazione del modello.
- Tecniche tipiche:
1. **Dati sintetici:** creazione artificiale di esempi per colmare scarsità dati e coprire casi rari.
2. **Back-translation:** traduzione in altra lingua e ritorno per ottenere parafrasi diverse.
3. **Synonym replacement:** sostituzione termini con sinonimi mantenendo il significato.
4. **Noise injection:** piccole perturbazioni (es. typo) per rendere il modello più robusto.
- Beneficio chiave: riduzione overfitting e supporto a lingue/domini con dati limitati.
- Attenzione: anche i dati sintetici richiedono controllo qualità e verifica bias.

**Distributed training e parallelismo**
- Per LLM di grandi dimensioni si distribuisce il training su più GPU.
- Principali strategie:
1. **Data parallelism:** il modello è replicato su più GPU; ogni GPU lavora su mini-batch diversi, poi sincronizza i gradienti.
2. **Model parallelism:** il modello è spezzato tra GPU diverse; utile quando non entra in una singola GPU.
3. **Pipeline parallelism:** il training è diviso in stadi sequenziali su processori/GPU diverse.
- Criticità: overhead di comunicazione e latenza rete; servono topologie/interconnessioni adeguate.

**Mixture of Experts (MoE)**
- Architettura con più subnet specializzate ("esperti").
- Per ogni input si attiva solo un sottoinsieme di esperti (sparse activation), non tutti.
- Risultato: più efficienza computazionale e memoria a parità di capacità complessiva.

**Nota manageriale sul pre-training**
- Nella maggior parte dei progetti aziendali il pre-training è gestito dal provider.
- Per l'AI PM è comunque essenziale capirne impatti indiretti: costi unitari, limiti tecnici, latenza e vincoli di scalabilità.

#### Post-training: adattare il modello al caso reale
**Fine-tuning**
- È la tecnica centrale del post-training: adatta un modello generale a task o dominio specifico aggiornando i pesi.
- I pesi sono i parametri numerici che governano il comportamento del modello.
- Modalità principali:
1. **Fine-tuning completo:** aggiorna tutti i parametri, massime prestazioni ma costo elevato.
2. **PEFT/LoRA:** aggiorna solo una piccola parte dei parametri (matrici aggiuntive), riducendo memoria e costi.

**Instruction tuning**
- Forma il modello a seguire meglio istruzioni utente su tono, formato, contesto e livello di dettaglio.
- È una base fondamentale per qualità conversazionale stabile in ambienti business.

**RLHF (Reinforcement Learning from Human Feedback)**
- Dopo pre-training/fine-tuning, valutatori umani (spesso SME) giudicano output per accuratezza, rilevanza e sicurezza.
- Questo feedback alimenta un reward model, poi usato in reinforcement learning per allineare il comportamento del modello.
- Beneficio: risposte più utili, meno output indesiderati, maggiore allineamento alle preferenze umane.

**Pruning**
- Riduce dimensione e complessità rimuovendo pesi, neuroni o layer poco utili.
- Processo tipico:
1. identificazione componenti ridondanti;
2. pruning strutturale o non strutturale;
3. nuovo fine-tuning per recuperare accuratezza;
4. iterazioni progressive per controllare il trade-off compressione/prestazioni.
- Utile per edge/mobile e scenari con hardware limitato.

**Distillation**
- Un modello "studente" più piccolo apprende il comportamento di un modello "docente" più grande.
- Obiettivo: ridurre costi di serving mantenendo qualità adeguata.
- Limite: su task molto complessi o specialistici il gap di qualità può aumentare.

**Quantization e QAT**
- Quantization: riduce precisione numerica (es. FP16, INT8) per abbassare memoria e calcolo.
- QAT (Quantization-Aware Training): prepara il modello alla quantizzazione già in training, riducendo perdita di qualità in deploy.
- Trade-off da governare: efficienza vs accuratezza.

**AI Red Teaming (Safety)**
- Test avversariali e di sicurezza per stressare il modello su scenari malevoli o limite.
- Non è solo "post-training": può essere continuo lungo tutto il lifecycle (prima, durante e dopo il go-live).

#### Inferenza: usare il modello in produzione
L'inferenza è la fase in cui il modello genera output su nuovi input reali senza aggiornare i parametri. Qui contano soprattutto latenza, costo per richiesta, qualità percepita e controllo del rischio.

#### Customization in inferenza
**Chunking**
- Spezza documenti lunghi in blocchi gestibili per retrieval e contesto.
- Essenziale in RAG quando la context window del modello è limitata.

**Hybrid search**
- Combina ricerca lessicale (keyword) e semantica (embedding).
- Migliora equilibrio precision/recall: match esatti + comprensione del significato.

**Reranking**
- Dopo il primo recupero documenti, un re-ranker riordina i candidati per rilevanza contestuale profonda.
- Aumenta precisione finale, con costo computazionale aggiuntivo.

#### Ottimizzazione in inferenza
**Semantic caching**
- Riutilizza risposte precedenti per richieste semanticamente simili.
- Riduce tempi e costo inferenziale nei casi ad alta ripetitività.

**Memory handling**
- Gestisce in modo efficiente cache, stato e memoria contestuale per task lunghi o complessi.
- Migliora coerenza su contenuti estesi e performance su conversazioni multi-turno.

**Batch parallelism**
- Elabora più richieste insieme sfruttando parallelismo hardware (GPU).
- Aumenta throughput, ma può introdurre attesa su singola richiesta e richiedere più memoria.

**Prompt optimization**
- Progettazione e miglioramento sistematico dei prompt per qualità/affidabilità migliori.
- Include anche compressione o riscrittura intelligente del prompt per ridurre costo e latenza.

**1-bit quantization**
- Quantizzazione estrema per inferenza molto efficiente anche su CPU.
- Può ridurre drasticamente requisiti hardware, ma richiede validazione rigorosa della qualità.

**Top-K sampling**
- Seleziona il token successivo tra i K più probabili, introducendo variabilità controllata.
- Utile quando serve creatività mantenendo coerenza.

**Beam search optimization**
- Mantiene più sequenze candidate e sceglie quella globalmente più probabile.
- Più deterministica e robusta su output lunghi/strutturati, ma più costosa.

**Container-level optimization**
- Ottimizzazioni di deployment/container: provisioning GPU, scheduling, scaling, configurazioni runtime e sicurezza.
- Obiettivo: migliorare stabilità, costo totale e performance in produzione.

#### Implicazioni per l'AI PM
1. Distinguere cosa è responsabilità provider (pre-training) e cosa è leva progettuale interna (post-training/inferenza).
2. Pianificare costi in scenari crescenti (pilot, ramp-up, produzione) con stime bottom-up.
3. Collegare ogni tecnica a KPI concreti: qualità, latenza, costo, sicurezza, compliance.
4. Introdurre escalation preventiva su rischi (guardrail tecnici, review aggiuntive, comitato governance).

#### Spiegazione dei termini (glossario operativo)
| Fase | Termine | Che cos'è | Perché conta nella gestione |
| --- | --- | --- | --- |
| Pre-training | SSL (Self-Supervised Learning) | Addestramento che usa etichette generate automaticamente dai dati stessi. | Riduce costo di etichettatura e abilita training su grandi volumi. |
| Pre-training | Vettorizzazione | Trasformazione di testo, immagini o segnali in vettori numerici elaborabili dal modello. | È la base tecnica che rende possibile training, retrieval e confronto semantico. |
| Pre-training | Embeddings | Rappresentazioni numeriche dense di parole, frasi, immagini o altri oggetti. | Determinano qualità di ricerca semantica, similarità e retrieval. |
| Pre-training | Multimodalità | Addestramento su più tipi di dati (testo, immagini, audio, video). | Abilita casi d'uso più ricchi e maggiore copertura di contesto. |
| Pre-training | Data augmentation | Tecniche per aumentare/variare i dati di training senza nuova raccolta massiva. | Migliora robustezza e generalizzazione del modello. |
| Pre-training | Dati sintetici | Dati artificiali generati per integrare dataset reali dove mancano volumi o casi rari. | Aiuta copertura scenari e test, ma richiede controllo qualità e bias. |
| Pre-training | Distributed training | Addestramento distribuito su più GPU/macchine in parallelo. | Riduce tempi di training ma aumenta complessità e costi infrastrutturali. |
| Pre-training | Mixture of Experts (MoE) | Architettura con più sotto-modelli specializzati attivati in modo selettivo. | Aumenta capacità del modello ottimizzando costo computazionale per richiesta. |
| Pre-training | Continuous pre-training | Ulteriore pre-training continuo su nuovi dati, senza entrare subito in fine-tuning task-specifico. | Mantiene il modello aggiornato su dominio e linguaggio in evoluzione. |
| Post-training | Fine-tuning | Adattamento del modello generale a dominio, task o stile specifico. | Aumenta qualità su casi reali aziendali. |
| Post-training | Instruction tuning | Variante di fine-tuning orientata a migliorare l'esecuzione di istruzioni utente. | Aumenta controllabilità e coerenza nei task conversazionali. |
| Post-training | PEFT/LoRA | Tecniche di fine-tuning leggero che aggiornano solo una piccola parte dei parametri. | Riduce costo computazionale e accelera iterazioni. |
| Post-training | RLHF | Allineamento del modello con feedback umano tramite reinforcement learning. | Migliora utilità percepita, tono e sicurezza dell'output. |
| Post-training | Pruning | Rimozione di pesi/connessioni poco utili nel modello. | Riduce dimensione e latenza con impatto controllato su performance. |
| Post-training | Distillation | Addestramento di un modello più piccolo a partire da uno più grande (teacher-student). | Mantiene buona qualità con costi di serving più bassi. |
| Post-training | Quantization | Riduzione della precisione numerica dei pesi (es. FP16/INT8). | Diminuisce memoria e costo inferenza, utile per produzione scalabile. |
| Post-training | Quantization-Aware Training (QAT) | Addestramento che prepara il modello alla quantizzazione già durante la fase di training. | Riduce perdita di qualità quando il modello viene compresso per la produzione. |
| Post-training | AI Red Teaming (Safety) | Test avversariali e di sicurezza per forzare il modello su casi pericolosi o limite. | Identifica vulnerabilità prima del rilascio e riduce rischio di abuso. |
| Inferenza | Chunking | Suddivisione documenti in blocchi più piccoli per retrieval e contesto. | Migliora reperimento informazioni e qualità risposte su knowledge base estese. |
| Inferenza | Hybrid search | Combinazione tra ricerca lessicale (keyword) e semantica (embedding). | Bilancia precisione su termini esatti e recall su significato. |
| Inferenza | Reranking | Riordinamento dei risultati recuperati con un modello più preciso. | Aumenta rilevanza finale delle fonti passate al modello. |
| Inferenza | Semantic caching | Riuso di risposte precedenti per richieste semanticamente simili. | Riduce latenza e costi operativi su prompt ricorrenti. |
| Inferenza | Memory handling | Gestione efficiente della memoria contestuale (cache e stato) durante la generazione. | Migliora performance su task lunghi e riduce degrado su finestre di contesto ampie. |
| Inferenza | Batch parallelism | Elaborazione simultanea di più richieste in batch. | Aumenta throughput e ottimizza uso hardware su carichi elevati. |
| Inferenza | Prompt optimization | Progettazione e miglioramento sistematico dei prompt per output migliori. | Riduce errori e variabilità senza dover riaddestrare il modello. |
| Inferenza | 1-bit quantization | Quantizzazione estrema che riduce drasticamente precisione numerica per efficienza massima. | Può abbassare molto costo e latenza, con trade-off da validare sulla qualità. |
| Inferenza | Top-K sampling | Decodifica che campiona il prossimo token tra i K più probabili. | Controlla creatività/varianza dell'output e limita risposte troppo casuali. |
| Inferenza | Beam search optimization | Decodifica che esplora più sequenze candidate e seleziona quelle globalmente migliori. | Aumenta coerenza su output complessi, a costo di maggiore computazione. |
| Inferenza | Container-level optimization | Ottimizzazioni di deployment a livello container/runtime (scaling, scheduling, risorse). | Migliora stabilità operativa, costi e tempi di risposta in produzione. |
| Inferenza | Parallelismo | Esecuzione simultanea di più richieste/elaborazioni in serving. | Aumenta throughput e supporta carichi elevati in produzione. |

Per il project manager, conoscere queste leve significa stimare meglio tempi, costi, rischi e dipendenze tra team.

### Checklist dei concetti principali
1. Definire use case e KPI business prima di aprire la sprint tecnica.
2. Verificare data readiness con criteri qualità espliciti.
3. Impostare baseline e target metrici realistici per ogni iterazione.
4. Integrare sicurezza, fairness e compliance nel piano di validazione.
5. Pianificare deploy graduale con monitoraggio e rollback.
6. Definire manutenzione, retraining e decommissioning fin dall'inizio.

### Lab consigliati per il Modulo 02
| Lab consigliato | Obiettivi | Categoria |
| --- | --- | --- |
| **[Deploy and Manage Generative AI Models](https://www.skills.google/paths/1283?catalog_rank=%7B%22rank%22%3A51%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&search_id=73610456)** | Collegare lifecycle tecnico e operativo: deploy, gestione versioni, monitoraggio e continuità in produzione. | Path |
| **[Get Started with Vertex AI Studio](https://www.skills.google/course_templates/723/labs/568846)** | Impostare prototipi in modo strutturato e trasformarli in sperimentazioni utili al ciclo progetto. | Lab |
| **[Generative AI with Vertex AI: Prompt Design](https://www.skills.google/course_templates/723/labs/568845)** | Migliorare qualità output e ridurre errori operativi tramite design, test e iterazione dei prompt. | Lab |
| **[Build and Deploy an Agent with Agent Engine in Vertex AI](https://www.skills.google/focuses/104687?catalog_rank=%7B%22rank%22%3A33%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=73610391)** | Comprendere il passaggio da sviluppo a rilascio in esercizio con dipendenze, integrazioni e controllo del rischio. | Focus |
| **[Get Started with Agent Development Kit (ADK)](https://www.skills.google/course_templates/1504/labs/599605)** | Applicare un flusso pratico di sviluppo e manutenzione agenti in logica iterativa e cross-funzionale. | Lab |

### Link utili del modulo
| Titolo | Descrizione | Link |
| --- | --- | --- |
| IBM SPSS Modeler - CRISP-DM Help Overview | Panoramica operativa della metodologia CRISP-DM in SPSS Modeler, utile per strutturare fasi, deliverable e governance del progetto IA. | [IBM Docs - CRISP-DM Help Overview](https://www.ibm.com/docs/it/spss-modeler/19.0.0?topic=dm-crisp-help-overview) |
| Azure MLOps Accelerator - Adopting Data Science Process | Guida pratica su ruoli, competenze e responsabilità nel ciclo MLOps per adottare un processo data science strutturato in team cross-funzionali. | [Azure MLOps Accelerator - Adopting DS Process](https://microsoft.github.io/azureml-ops-accelerator/1-MLOpsFoundation/2-SkillsRolesAndResponsibilities/1-AdoptingDSProcess.html) |
| CRISP-ML(Q) Framework | Estensione di CRISP-DM orientata al machine learning con enfasi su qualità del modello, monitoraggio e gestione del rischio lungo il lifecycle. | [CRISP-ML(Q) - MLOps.org](https://ml-ops.org/content/crisp-ml) |
| NIST AI Risk Management Framework (AI RMF 1.0) | Framework di riferimento per identificare, valutare e gestire i rischi AI lungo l'intero ciclo di vita con un approccio governance-first. | [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) |
| Ethics Guidelines for Trustworthy AI (EU) | Linee guida europee sull'AI affidabile con principi etici, requisiti pratici e indicazioni per l'implementazione responsabile nei progetti IA. | [European Commission - Ethics Guidelines for Trustworthy AI](https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai) |
| Google Responsible AI (Generative AI) | Documentazione pratica di Google sui principi e controlli per sviluppare applicazioni generative in modo responsabile, sicuro e verificabile. | [Google AI - Responsible AI Docs](https://ai.google.dev/responsible/docs) |
| Impatto ambientale dell'AI (Tinnovamag) | Articolo divulgativo con grafico riepilogativo sull'impatto ambientale dell'AI, utile come supporto di sensibilizzazione nella discussione su sostenibilità del progetto. | [Tinnovamag - Impatto ambientale dell'AI](https://tinnovamag.com/a-quanto-ammonta-limpatto-ambientale-dellai/) |
| Microsoft Fairwater: datacenter AI in Wisconsin | Notizia su Fairwater, presentato come grande iniziativa infrastrutturale AI; utile per contestualizzare la crescita del fabbisogno computazionale e i temi di sostenibilità/consumi energetici. | [HWUpgrade - Microsoft presenta Fairwater](https://www.hwupgrade.it/news/server-workstation/microsoft-presenta-fairwater-il-piu-potente-datacenter-ai-al-mondo-nasce-in-wisconsin_143754.html) |
| MIT AI Risk Repository | Repository strutturato dei rischi AI utile per identificare pattern di rischio e allineare controlli di governance/mitigazione. | [MIT AI Risk Repository](https://airisk.mit.edu/) |
| Video - Come usare AI Risk Repository | Video introduttivo per comprendere struttura, logica di classificazione e uso operativo del risk repository nei progetti AI. | [YouTube - AI Risk Repository walkthrough](https://www.youtube.com/watch?v=fCj-wJz6VCY) |
| ISO/IEC 42001 - AI Management System | Standard internazionale per impostare un sistema di gestione dell'AI con requisiti organizzativi, controlli e miglioramento continuo. | [ISO/IEC 42001 - Standard](https://www.iso.org/es/contents/data/standard/08/11/81118.html) |
| ISO Standard 83002 | Riferimento ISO su governance e gestione del rischio AI da usare come supporto nella definizione di controlli e policy operative. | [ISO Standard 83002](https://www.iso.org/standard/83002.html) |
| Operationalizing AI (O'Reilly) | Guida pratica per portare sistemi AI in produzione con focus su MLOps, processi operativi, monitoraggio e gestione del rischio. | [Operationalizing AI - O'Reilly](https://learning.oreilly.com/library/view/operationalizing-ai/9781098101329/) |
| Responsible AI Toolbox | Raccolta di strumenti pratici per valutare e monitorare qualità, fairness, interpretabilità e analisi degli errori nei modelli AI durante validazione e monitoraggio. | [Responsible AI Toolbox](https://responsibleaitoolbox.ai/) |
| Responsible AI Dashboard Tour (Tabular) | Notebook ufficiale con tour guidato del Responsible AI Dashboard su dati tabellari: setup, metriche, fairness, error analysis e interpretabilità. | [Responsible AI Dashboard Tour - Notebook](https://github.com/microsoft/responsible-ai-toolbox/blob/main/notebooks/responsibleaidashboard/tabular/tour.ipynb) |

## Modulo 03: Integrazione GenAI in processi aziendali
### Scheda rapida del modulo
- **Obiettivo:** integrare modelli linguistici nei processi aziendali con equilibrio tra qualità, costo, controllo e velocità.
- **Focus manageriale:** scegliere il pattern di integrazione corretto, impostare valutazione robusta e guidare il miglioramento continuo.
- **Output atteso:** una roadmap pratica per selezione modello, messa in produzione, monitoraggio e ottimizzazione.

### Come funziona un language model e perché impatta il prodotto
Un language model genera testo prevedendo token plausibili in base al contesto. Questo meccanismo sembra semplice, ma in azienda determina aspetti decisivi: affidabilità delle risposte, aderenza alle regole, latenza, costi operativi, qualità percepita dagli utenti.

Per un team di prodotto è fondamentale distinguere due livelli:
1. **Capacità generali del modello** (linguaggio, ragionamento, comprensione istruzioni).
2. **Capacità operative nel tuo contesto** (tono brand, accuratezza sui dati interni, robustezza su casi reali).

La differenza tra questi due livelli spiega perché un modello brillante in demo può fallire in produzione.

![Confronto tra risposta linguistica grezza e risposta conversazionale](assets/chapt05_images/ch05_img01.png)
*Figura M3.1: un modello addestrato solo sul completamento linguistico può produrre output corretti ma poco utili alla conversazione*

![Confronto con modello ottimizzato per dialogo naturale](assets/chapt05_images/ch05_img07.png)
*Figura M3.2: dopo ottimizzazioni orientate all'interazione umana la qualità conversazionale aumenta sensibilmente*

### Dati di training: dove nascono qualità e rischio
Le prestazioni di un sistema GenAI dipendono in modo diretto dai dati di addestramento. Prima dell'integrazione bisogna valutare almeno cinque dimensioni:

1. **Scala e diversità:** più copertura significa maggiore versatilità, ma non garantisce precisione in domini verticali.
2. **Bias e stereotipi:** il modello può riflettere squilibri presenti nei dati e generare risposte discriminatorie.
3. **Rumore e qualità:** fonti non verificate possono introdurre errori plausibili ma falsi.
4. **Knowledge cutoff:** senza basi aggiornate il modello non conosce eventi recenti.
5. **Privacy e proprietà intellettuale:** occorre verificare uso di dati sensibili e vincoli legali.

Per questo la scelta del modello non è mai solo tecnica: è una decisione di governance che richiede coinvolgimento congiunto di prodotto, legale, sicurezza e data team.

### Obiettivo di training e comportamento del modello
I modelli possono essere ottimizzati con obiettivi diversi. Comprendere l'obiettivo aiuta a prevedere punti forti e limiti:

- **Autoregressivo:** predice il prossimo token; ottimo per generazione e dialogo.
- **Autoencoding:** ricostruisce token mancanti usando contesto bidirezionale; utile per compiti analitici.
- **Sequence-to-sequence:** trasforma un input in un output strutturalmente diverso; efficace su traduzione, sintesi, trasformazioni.

![Obiettivo di language modeling basato sul contesto](assets/chapt05_images/ch05_img12.png)
*Figura M3.3: il modello stima il token successivo usando il contesto disponibile*

![Relazioni semantiche bidirezionali nella frase](assets/chapt05_images/ch05_img13.png)
*Figura M3.4: le dipendenze linguistiche non sono solo in avanti, ma anche all'indietro*

### Allucinazioni: gestione operativa del rischio
Le allucinazioni sono output fluenti ma errati: fatti inventati, citazioni inesistenti, nessi causali non dimostrati, contraddizioni logiche. In contesti aziendali questo rischio impatta reputazione, compliance e decisioni.

Contromisure da standardizzare:
1. validazione con fonti autorevoli;
2. retrieval su basi documentali affidabili;
3. istruzioni di sistema più restrittive;
4. revisioni umane su casi ad alto impatto;
5. dataset correttivi per ridurre errori ricorrenti.

### Pattern di integrazione: scegliere l'architettura giusta
L'integrazione GenAI non è unica: dipende da input, output, livello di rischio e criticità del processo. I tre pattern più utili sono:

1. **Interazione diretta utente-modello** per casi aperti e creativi.
2. **Uso programmatico** con output eseguibile (funzioni, query, comandi).
3. **Task predefiniti backend** per processi controllati e auditabili.

![Tre pattern tipici d'uso dei language model](assets/chapt05_images/ch05_img09.png)
*Figura M3.5: i pattern d'uso variano per apertura di input/output e complessità di controllo*

#### Pattern 1: interazione diretta
È il pattern più diffuso nei chatbot e assistenti di produttività, ma anche il più delicato: input imprevedibili, ampio spazio di output, maggiore esposizione a prompt avversariali e contenuti non conformi.

![Interazione diretta tra utente e modello](assets/chapt05_images/ch05_img15.png)
*Figura M3.6: esposizione diretta del modello all'utente finale*

Per ridurre costo e rischio si possono usare orchestrazioni multi-modello:
- **Router LM:** instrada la richiesta verso il modello più adatto.
- **Cascade LM:** parte da modelli economici e scala a modelli più potenti solo quando serve.
- **Human-in-the-loop:** inoltra casi complessi a operatori umani.

![Pattern router per instradamento richieste](assets/chapt05_images/ch05_img05.png)
*Figura M3.7: il router seleziona modello o operatore in base al tipo di richiesta*

![Pattern cascade con escalation progressiva](assets/chapt05_images/ch05_img11.png)
*Figura M3.8: la richiesta passa a modelli più avanzati finché non raggiunge confidenza adeguata*

#### Pattern 2: uso programmatico
Qui il modello genera output strutturati o codice che viene eseguito da sistemi downstream. È potente ma richiede guardrail stringenti:
- schema obbligatorio (JSON, function-calling, output contract);
- validazione sintattica e semantica prima dell'esecuzione;
- policy di autorizzazione per evitare azioni distruttive;
- log completo per audit e incident analysis.

![Generazione di codice con esecuzione automatica a valle](assets/chapt05_images/ch05_img08.png)
*Figura M3.9: output del modello usato come input operativo di altri componenti*

#### Pattern 3: task predefiniti in backend
Il modello lavora su compiti circoscritti (classificazione, sintesi, estrazione, sentiment), con input controllati e validazione a monte e a valle. Spesso è il pattern migliore per scenari enterprise B2B dove affidabilità e tracciabilità sono prioritarie.

![Uso del modello in pipeline offline con controlli aggiuntivi](assets/chapt05_images/ch05_img04.png)
*Figura M3.10: esecuzione offline per aumentare controllo qualità e ridurre rischio operativo*

### Panorama modelli: come orientarsi senza dispersione
Per selezionare il modello è utile classificare le opzioni in cinque famiglie operative:

| Categoria | Vantaggi principali | Limiti principali | Quando usarla |
| --- | --- | --- | --- |
| LLM commerciali via API | time-to-market rapido, ottime prestazioni generaliste | costi variabili, minore controllo interno | avvio progetto, test di fattibilità, MVP |
| Modelli open source | maggiore controllo, possibilità di personalizzazione profonda | maggiore complessità infrastrutturale | casi con requisiti di privacy, governance o costo unitario |
| Modelli reasoning | maggiore trasparenza su passaggi logici in alcuni task | latenza e costo spesso superiori | compiti con elevata richiesta di spiegabilità |
| Small language model | efficienza, bassa latenza, deploy locale più semplice | capacità inferiore su task complessi | automazioni verticali e ad alto volume |
| Modelli multimodali | uniscono testo, immagine, audio/video | infrastruttura più pesante | casi d'uso multicanale e workflow creativi avanzati |

![Esempio di modello con ragionamento esplicito](assets/chapt05_images/ch05_img14.png)
*Figura M3.11: modello reasoning con passaggi argomentativi più leggibili*

### Lifecycle operativo del language model
La gestione efficace segue un ciclo iterativo, non lineare:
1. selezione iniziale;
2. valutazione tecnica e business;
3. personalizzazione;
4. rilascio controllato;
5. raccolta feedback;
6. ottimizzazione continua.

![Ciclo iterativo di sviluppo e miglioramento del modello](assets/chapt05_images/ch05_img03.png)
*Figura M3.12: lifecycle di integrazione e ottimizzazione continua*

### Selezione modello: criteri decisionali concreti
Un framework utile per il team:
1. **Vincoli non negoziabili:** compliance, localizzazione dati, policy interne.
2. **Obiettivi utente:** qualità percepita, affidabilità, tempo di risposta.
3. **Obiettivi economici:** costo per richiesta, costo mensile, costo di gestione.
4. **Scalabilità tecnica:** throughput, disponibilità, piano di fallback.
5. **Evoluzione prevista:** possibilità di passare a setup multi-modello nel tempo.

Una pratica efficace è partire con una shortlist di 2-3 modelli, testati sul dataset reale del processo target e su prompt rappresentativi del traffico effettivo.

Approfondimento consigliato per la fase di selezione:
- [Choosing the Right Language Model for Your NLP Use Case](https://medium.com/data-science/choosing-the-right-language-model-for-your-nlp-use-case-1288ef3c4929)
- [Create a RAG Application with BigQuery](https://www.skills.google/focuses/117532?catalog_rank=%7B%22rank%22%3A1%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=75402418)

### Valutazione: benchmark pubblici + metriche personalizzate
I benchmark pubblici sono un punto di partenza, non il punto d'arrivo. Servono per confronto iniziale, ma non sostituiscono la misurazione su casi reali aziendali.

![Esempio di confronto modelli su benchmark pubblici](assets/chapt05_images/ch05_img10.png)
*Figura M3.13: benchmark comparativi utili per la prima scrematura*

Metriche da presidiare in combinazione:
- **accuratezza fattuale** (groundedness, error rate);
- **aderenza al compito** (task completion);
- **qualità linguistica** (coerenza, leggibilità, tono);
- **rischio** (violazioni policy, contenuti impropri, fallimenti critici);
- **performance tecnica** (latenza, stabilità, costo per richiesta).

Per rendere la valutazione robusta conviene adottare un approccio ibrido:
1. valutazione automatica su volumi elevati;
2. revisione umana su campioni strategici;
3. stress test su edge case e prompt avversariali.

![Tradeoff velocità-affidabilità nei metodi di valutazione](assets/chapt05_images/ch05_img02.png)
*Figura M3.14: bilanciamento tra velocità di valutazione e affidabilità del giudizio*

### Personalizzazione: prompt, retrieval, fine-tuning
Le tre leve principali hanno difficoltà e impatto differenti:

1. **Prompt engineering:** rapido, economico, utile per regolare stile e formato.
2. **RAG:** migliora accuratezza e aggiornamento attingendo a fonti controllate.
3. **Fine-tuning:** più impegnativo, ma decisivo per comportamento stabile e dominio specifico.

![Livelli di personalizzazione: prompt, RAG, fine-tuning](assets/chapt05_images/ch05_img06.png)
*Figura M3.15: tecniche di personalizzazione in ordine crescente di profondità tecnica*

### Feedback in produzione e ottimizzazione continua
La qualità reale emerge in esercizio. Occorre impostare un loop continuo:

1. raccogliere feedback espliciti (rating, segnalazioni, revisione operatori);
2. osservare segnali impliciti (abbandono flusso, correzioni manuali, tempo task);
3. classificare errori per priorità di impatto;
4. introdurre dati correttivi e nuove regole di orchestrazione;
5. rieseguire test di regressione prima di ogni rilascio.

Quando possibile, automatizzare monitoraggio, validazione e aggiornamenti con pratiche LLMOps riduce il tempo tra problema osservato e miglioramento rilasciato.

### Sintesi operativa intermedia del Modulo 03
1. Definire pattern di integrazione per ogni processo (diretto, programmatico, backend).
2. Esplicitare rischi e guardrail prima del go-live.
3. Selezionare modelli con criteri condivisi tra business, engineering e compliance.
4. Validare su benchmark e su dataset reale del dominio.
5. Attivare metriche continue su qualità, rischio, latenza e costo.
6. Pianificare iterazioni periodiche su prompt, retrieval e tuning.

### Prompt Engineering per processi aziendali
Quando il modello è già scelto, la leva più rapida per migliorare qualità e controllo è il prompt engineering. In pratica significa progettare istruzioni, contesto ed esempi in modo sistematico, così da trasformare output generici in output coerenti con obiettivi di business, tono, vincoli normativi e formato operativo.

L'approccio corretto non è scrivere prompt "ispirati", ma costruire un ciclo disciplinato: ipotesi, test, misurazione, revisione e standardizzazione.

![Panoramica delle principali tecniche di prompting](assets/chapt06_images/ch06_img06.png)
*Figura M3.16: mappa delle tecniche di prompting dal livello base a quello avanzato*

### Livello base: zero-shot prompting
Lo zero-shot è il punto di partenza: si chiede al modello di svolgere un compito senza esempi dimostrativi. È ideale per attività semplici o già ben rappresentate nelle capacità native del modello.

Esempi tipici in azienda:
- classificare rapidamente ticket cliente per priorità;
- sintetizzare note riunione in azioni operative;
- produrre una prima bozza di comunicazione interna.

Il limite dello zero-shot è la variabilità: se il task richiede stile specifico, rigore formale o precisione su dominio verticale, spesso serve una struttura più ricca.

![Schema di prompt input-output per task semplice](assets/chapt06_images/ch06_img07.png)
*Figura M3.17: struttura essenziale del prompting zero-shot*

### Struttura modulare del prompt
Per rendere il prompting ripetibile serve scomporre ogni prompt in componenti standard:

1. **Contesto:** ruolo, scenario, obiettivo e vincoli.
2. **Istruzione:** cosa fare, in che ordine, con quale livello di dettaglio.
3. **Esempi:** dimostrazioni di output desiderato.
4. **Variabili input:** dati dinamici del caso reale.
5. **Formato output:** schema finale (testo continuo, tabella, JSON, checklist).
6. **Constraint:** limiti su lunghezza, tono, lessico, confidenza, esclusioni.

Questa modularità rende più semplice collaborare tra team, mantenere coerenza e ridurre regressioni durante gli aggiornamenti.

![Schema di few-shot prompting con esempi](assets/chapt06_images/ch06_img02.png)
*Figura M3.18: i prompt con esempi guidano il modello per analogia*

![Visuale di workflow per selezione esempi in few-shot automatico](assets/chapt06_images/ch06_img01.png)
*Figura M3.19: pipeline di recupero automatico degli esempi più utili*

### Few-shot prompting: quando e come usarlo
Il few-shot migliora la qualità quando lo stile o la logica del compito non emergono bene con una sola istruzione. Funziona bene per:
- contenuti marketing con tono preciso;
- classificazioni con etichette aziendali specifiche;
- trasformazioni di testo con regole redazionali definite.

Tre attenzioni operative:
1. **Costo token:** troppi esempi aumentano latenza e costo.
2. **Bias da ordine/esempi:** sequenza e distribuzione influenzano il risultato.
3. **Manutenzione:** esempi vecchi degradano la qualità nel tempo.

Per scalare, conviene costruire una libreria versionata di esempi e recuperare in automatico solo i più pertinenti al caso corrente.

### Reasoning guidato: chain-of-thought, self-consistency, reflection
Per task complessi il modello deve "pensare a passi". Invece di chiedere subito l'output finale, si imposta un percorso ragionato che riduce errori logici.

![Schema di chain-of-thought per decomposizione del compito](assets/chapt06_images/ch06_img04.png)
*Figura M3.20: scomporre il problema in step aumenta affidabilità sui task multi-passaggio*

Con **self-consistency** si generano più varianti e si seleziona la migliore tramite voto, scoring o valutazione comparativa. È utile per creatività controllata e per casi in cui serve scegliere l'opzione più robusta.

![Schema di self-consistency con confronto di più varianti](assets/chapt06_images/ch06_img03.png)
*Figura M3.21: più campioni, valutazione strutturata, selezione dell'output migliore*

Il **double diamond** aiuta a usare la self-consistency in modo manageriale: prima si esplora lo spazio problema, poi lo spazio soluzioni, convergendo in modo esplicito su una scelta.

![Double diamond per divergenza e convergenza nel processo creativo](assets/chapt06_images/ch06_img05.png)
*Figura M3.22: metodo pratico per passare da molte ipotesi a una decisione finale*

La **reflection** completa il ciclo: il modello valuta il proprio output su criteri prefissati (chiarezza, completezza, azionabilità), individua gap e propone revisione. In produzione, questo passaggio migliora la qualità senza dover sempre cambiare modello.

### Prompting per output strutturati e automazione
Nei processi aziendali, spesso l'output deve essere riusabile da sistemi downstream. Per questo il prompt deve specificare schema e vincoli di formato:
- campi obbligatori;
- tipi di dato attesi;
- valori ammessi;
- regole di fallback in caso di informazione mancante.

Questa impostazione abilita integrazione con workflow automatici, dashboard, reportistica e controlli qualità.

### Best practice operative di team
Per evitare caos nel prompting, impostare uno standard di lavoro:

1. **Conoscere bene il modello:** limiti, bias, knowledge cutoff, latenza e costi.
2. **Lavorare in modo interdisciplinare:** prodotto, dominio, engineering, compliance.
3. **Scrivere prompt specifici e contestualizzati:** ridurre ambiguità e supposizioni.
4. **Versionare tutto:** prompt, esempi, metriche, dataset di test e risultati.
5. **Valutare in modo continuo:** test suite con casi normali, edge case e input avversariali.
6. **Monitorare in produzione:** intercettare domain shift e aggiornare template/esempi.

### Dalla sperimentazione alla governance del prompting
Nelle fasi iniziali è normale lavorare in modo esplorativo. Ma quando il sistema entra in produzione, il prompting va gestito come asset critico:

- repository centralizzato di template;
- naming convention e ownership chiari;
- processo di review e approvazione;
- metriche di qualità collegate a KPI di business;
- rollback rapido in caso di regressioni.

In questo modo il prompting smette di essere un'attività artigianale e diventa una capacità organizzativa stabile, misurabile e scalabile.

### Punti operativi per integrazione Prompt Engineering
1. Definire template base per i principali processi (supporto, vendita, operation, compliance).
2. Stabilire criteri di qualità misurabili per ogni template.
3. Costruire una libreria di esempi con tag per dominio, tono e complessità.
4. Introdurre strategie di reasoning solo dove il beneficio supera il costo.
5. Richiedere output strutturati quando il risultato alimenta sistemi automatici.
6. Pianificare monitoraggio continuo con correzione periodica di prompt e dataset esempi.

### Search semantico e RAG: integrare conoscenza aziendale nel flusso GenAI
Quando i contenuti generati risultano troppo generici, il problema non è solo il modello: manca l'accesso strutturato alla conoscenza interna dell'azienda. La Retrieval-Augmented Generation (RAG) risolve questo gap collegando i prompt a dati proprietari aggiornati.

In pratica:
1. recuperi i documenti più rilevanti per la richiesta;
2. li inserisci nel contesto del prompt;
3. generi una risposta ancorata alle fonti recuperate.

![Dal search semantico a un sistema RAG completo](assets/chapt07_images/ch07_img09.png)
*Figura M3.24: evoluzione dall'information retrieval alla generazione con contesto recuperato*

![Lifecycle operativo di un sistema RAG](assets/chapt07_images/ch07_img10.png)
*Figura M3.25: fasi iterative per progettare, valutare e ottimizzare la pipeline RAG*

Un esempio molto chiaro di differenza tra modello "isolato" e modello con grounding è questo:
- se chiedi **"When was the last chinese new year?"** a un modello senza grounding, la risposta tende a riflettere la **data di cutoff** della conoscenza disponibile nel modello;
- nel caso mostrato, senza grounding il modello restituisce **10 febbraio 2024**, che era l'ultimo capodanno cinese noto nel suo perimetro di conoscenza;
- quando invece attivi il grounding con un tool di **web search**, il modello esegue prima una ricerca sul web e costruisce la risposta su fonti aggiornate;
- nello stesso esempio, con grounding la risposta diventa **17 febbraio 2026**, cioè il dato più recente recuperato online.

Questo esempio è utile perché rende visibile un punto progettuale essenziale: il grounding non serve solo a "citare fonti", ma anche a **superare il limite temporale della conoscenza statica del modello**. In tutti i casi d'uso dove contano date, eventi recenti, prezzi, norme o informazioni che cambiano nel tempo, affidarsi al solo modello espone a risposte fluenti ma non aggiornate.

Dal punto di vista operativo, il messaggio per il team è semplice:
1. se la domanda riguarda conoscenza relativamente stabile, il modello può bastare;
2. se la domanda dipende da dati recenti o variabili, serve grounding su fonti affidabili;
3. se la risposta ha impatto operativo o decisionale, grounding e tracciabilità delle fonti diventano requisiti di qualità, non optional.

![Confronto tra risposta senza grounding e risposta grounding-aware con web search](assets/chapt03_images/grounding_web_search_cutoff_example_m03.png)
*Figura M3.25b: senza grounding il modello riflette il proprio cutoff di conoscenza; con grounding via web search recupera l'informazione più aggiornata disponibile*

![Schermata di configurazione di una Search App per grounding in Google Cloud AI Applications](assets/chapt03_images/search_app_grounding_builder_m03.png)
*Figura M3.25c: esempio di costruzione di una Search App per collegare grounding, configurazione dell'interfaccia e test della ricerca su fonti indicizzate*

![Preview del risultato di una query grounding-aware in una Search App](assets/chapt03_images/search_app_grounding_preview_result_m03.png)
*Figura M3.25d: esempio di risposta recuperata dalla Search App, utile per verificare qualità del retrieval, pertinenza dei contenuti e esperienza utente del RAG*

![Confronto tra risposta senza grounding e risposta con grounding su Search App per il caso Cymbal](assets/chapt03_images/search_app_grounding_cymbal_compare_m03.png)
*Figura M3.25e: senza grounding il modello allucina sul caso Cymbal; con grounding tramite Search App recupera informazioni corrette e cita le risorse usate nella risposta*

### Perché il prompting da solo non basta nel tempo
Il prompting migliora stile e struttura, ma non crea nuova conoscenza affidabile. Quando l'utente richiede dati specifici di settore, procedure interne o informazioni recenti, serve una pipeline che recuperi fonti pertinenti prima della generazione.

Segnali tipici che indicano necessità di RAG:
- output fluenti ma poco specifici sul dominio;
- alto lavoro di post-editing da parte dei team;
- riferimenti incompleti o non aggiornati;
- difficoltà nel riuso della conoscenza distribuita tra wiki, CRM, drive e ticketing.

### Embeddings: la base del recupero semantico
Il search semantico rappresenta testi e query come vettori (embeddings). La vicinanza tra vettori riflette la somiglianza di significato, non solo la corrispondenza lessicale.

![Parole simili vicine nello spazio vettoriale](assets/chapt07_images/ch07_img11.png)
*Figura M3.26: similarità semantica come distanza tra embeddings*

![Frasi raggruppate per prossimità semantica](assets/chapt07_images/ch07_img04.png)
*Figura M3.27: clustering di frasi con contenuto affine nello spazio embedding*

Per un team prodotto questo implica una decisione importante: scegliere modello embedding, granularità dei chunk e strategia di indicizzazione incide direttamente su precisione, costo e latenza.

### Costruzione della base documentale
La pipeline minima di retrieval include:
1. ingestione da sorgenti aziendali;
2. pulizia e normalizzazione dei documenti;
3. chunking dei testi;
4. generazione embeddings;
5. salvataggio in database vettoriale.

![Processo di costruzione dell'embedding database](assets/chapt07_images/ch07_img02.png)
*Figura M3.28: passaggi per trasformare documenti eterogenei in indice interrogabile*

Scelte operative da governare:
- **chunking:** troppo corto perde contesto, troppo lungo introduce rumore;
- **database vettoriale:** differenze su scalabilità, filtri, costi operativi;
- **metadati:** fondamentali per filtrare per lingua, data, prodotto, business unit.

### Come funziona il search semantico in produzione
La query utente viene embedded e confrontata con i vettori indicizzati; il sistema restituisce i top-k chunk più pertinenti.

![Pipeline di semantic search](assets/chapt07_images/ch07_img03.png)
*Figura M3.29: retrieval top-k per similarità semantica tra query e chunk*

Valutazione minima del retrieval:
- **precision@k:** quota di risultati rilevanti nei primi k;
- **recall@k:** copertura dei documenti rilevanti;
- **MRR:** qualità della posizione del primo risultato corretto.

### Ottimizzazione del retrieval
Dopo la baseline, il recupero va affinato in modo sistematico:

1. **chunking avanzato** per preservare confini semantici;
2. **contestualizzazione dei chunk** con brevi prefissi descrittivi;
3. **ricerca ibrida** (semantica + lessicale) per aumentare precisione su termini esatti;
4. **filtri metadato** per restringere il dominio utile;
5. **reranking** per ordinare meglio risultati quasi equivalenti.

![Recap del sistema di search e aree di miglioramento](assets/chapt07_images/ch07_img05.png)
*Figura M3.30: mappa delle principali leve di ottimizzazione del retrieval*

![Integrazione tra ricerca semantica e lessicale](assets/chapt07_images/ch07_img06.png)
*Figura M3.31: la strategia ibrida migliora il bilanciamento tra richiamo e precisione*

### Dalla ricerca al RAG end-to-end
Il passo successivo è collegare retrieval e generazione in un unico flusso:
1. query utente;
2. recupero chunk rilevanti;
3. costruzione prompt aumentato;
4. generazione risposta con riferimenti alle fonti.

![Schema di sistema RAG end-to-end](assets/chapt07_images/ch07_img08.png)
*Figura M3.32: pipeline completa dalla richiesta utente alla risposta grounding-aware*

Nella costruzione prompt conviene separare:
- **system instruction:** regole di comportamento e uso delle fonti;
- **task instruction:** output atteso e livello di dettaglio;
- **context block:** estratti recuperati e metadati citabili;
- **constraints:** vincoli su citazioni, tono, formato e limiti di inferenza.

### Valutazione del RAG: componenti + end-to-end
La qualità va misurata su due livelli:
1. **component-level:** retrieval e generazione valutati separatamente;
2. **end-to-end:** risposta finale valutata rispetto alla query reale.

Metriche prioritarie:
- **context relevance:** pertinenza dei chunk recuperati;
- **groundedness:** aderenza dell'output alle fonti;
- **answer relevance:** capacità di rispondere davvero alla richiesta.

Per scalare i test si può usare valutazione assistita da LLM, mantenendo un campione con revisione umana per intercettare bias del giudice automatico.

### Ottimizzare il RAG in modo continuo
Una volta in produzione, le leve più efficaci sono:

1. **query enhancement:** riscrittura/espansione query troppo vaghe;
2. **prompt adaptation:** vincoli dinamici in base al caso d'uso (esplorativo vs strettamente documentale);
3. **context curation:** deduplicazione e fusione dei contenuti recuperati;
4. **multi-turn retrieval:** recuperi iterativi per compiti complessi;
5. **GraphRAG:** uso di relazioni esplicite tra entità per query multi-hop;
6. **fine-tuning mirato:** quando serve profondità di dominio non ottenibile con retrieval e prompt.

![Leve di ottimizzazione di un sistema RAG](assets/chapt07_images/ch07_img01.png)
*Figura M3.34: aree prioritarie per aumentare qualità, affidabilità e coerenza delle risposte*

### Punti operativi per integrazione RAG
1. Definire use case e livelli di rischio prima della scelta architetturale.
2. Stabilire strategia chunking, metadati e aggiornamento indice.
3. Misurare retrieval con metriche quantitative già nella fase prototipale.
4. Separare template prompt per casi con forte grounding e casi esplorativi.
5. Introdurre monitoraggio continuo di groundedness e answer relevance.
6. Pianificare cicli periodici di ottimizzazione su query, retrieval e generazione.

### Agentic AI: automatizzare workflow complessi
Con i sistemi agentici l'IA non si limita a generare testo, ma orchestra azioni su strumenti esterni per completare task multi-step. Questo abilita automazioni che prima richiedevano passaggi manuali distribuiti tra più applicazioni.

In un flusso enterprise la differenza pratica è questa:
- workflow manuale: l'utente coordina ricerca, analisi, decisione e comunicazione;
- workflow agentico: l'utente imposta obiettivo e vincoli, l'agente gestisce esecuzione e ritorna output strutturato.

![Workflow umano vs workflow con agente LM](assets/chapt09_images/ch09_img08.png)
*Figura M3.35: confronto tra esecuzione manuale e orchestrazione automatizzata tramite agente*

![Esempio di task prompt per agente di product management](assets/chapt09_images/ch09_img10.png)
*Figura M3.36: prompt iniziale che definisce obiettivo, contesto e vincoli operativi dell'agente*

### Tool access: la base dell'azione nel mondo reale
Un agente diventa utile quando può usare strumenti esterni in modo controllato. Le categorie operative principali sono:

1. **Strumenti di lettura dati**: search, basi documentali, CRM, ticketing, data warehouse.
2. **Strumenti di analisi**: SQL, modelli predittivi, motori di regole, calcolo.
3. **Strumenti di azione**: email, Slack, sistemi di workflow, update documentali.
4. **Strumenti umani (HITL)**: richiesta di validazione quando confidenza o impatto non sono adeguati.

![Template roadmap usato come output target dell'agente](assets/chapt09_images/ch09_img12.png)
*Figura M3.37: esempio di artefatto finale che l'agente deve produrre e mantenere*

![Integrazione di più categorie di tool nell'agente](assets/chapt09_images/ch09_img11.png)
*Figura M3.38: estensione progressiva del tool stack per coprire raccolta, analisi e coordinamento*

### Modello di automazione progressiva
Nei contesti reali conviene partire con automazione parziale, poi aumentare autonomia quando qualità e affidabilità diventano stabili.

Approccio consigliato:
1. avvio con task a basso rischio e output review obbligatoria;
2. automazione di task ripetitivi con validazione a campione;
3. introduzione di azioni write-enabled solo con guardrail forti;
4. monitoraggio continuo di errori, escalation e rollback.

![Riduzione progressiva del coinvolgimento umano con aumento affidabilità](assets/chapt09_images/ch09_img14.png)
*Figura M3.39: transizione da interfaccia ad alta supervisione a interfaccia semplificata*

### Ecosistema tool e funzione di orchestrazione
Ogni integrazione esterna va trattata come componente critico di prodotto: SLA, qualità, sicurezza, fallback e costo. Gli agenti funzionano meglio quando il catalogo strumenti è limitato e ben curato.

![Ecosistema plug-in/tool disponibili per estendere gli agenti](assets/chapt09_images/ch09_img15.png)
*Figura M3.40: panorama integrazioni esterne che l'agente può invocare*

Il ciclo base di tool use è:
1. selezione dello strumento corretto;
2. invocazione con parametri validi;
3. parsing del risultato e decisione del passo successivo.

![Processo decisionale di un agente nell'uso di uno strumento](assets/chapt09_images/ch09_img02.png)
*Figura M3.41: flow minimo di selezione, esecuzione e interpretazione output del tool*

### Architettura dell'agente: componenti essenziali
Un agente robusto combina quattro blocchi:
- **LM controller** per ragionamento e orchestrazione;
- **tool layer** per accesso a dati e azioni;
- **planning module** per decomporre task complessi;
- **memory module** per continuità e apprendimento.

![Architettura ad alto livello di un agente](assets/chapt09_images/ch09_img01.png)
*Figura M3.42: componenti principali e flussi tra modello, memoria, piano e strumenti*

![Interazione agente-ambiente esterno](assets/chapt09_images/ch09_img04.png)
*Figura M3.43: ciclo osservazione-decisione-azione con feedback dal contesto operativo*

### Pianificazione: da task ampio a piano eseguibile
Senza pianificazione i sistemi agentici degradano in tentativi disordinati. La pipeline corretta prevede:
1. decomposizione del problema;
2. ordinamento dei sottotask;
3. selezione tool per ciascun sottotask;
4. controlli di coerenza tra step;
5. consolidamento output finale.

![Template prompt per governare la pianificazione dell'agente](assets/chapt09_images/ch09_img03.png)
*Figura M3.44: struttura prompt per guidare la pianificazione in modo ripetibile*

![Metodi di pianificazione disponibili per gli agenti](assets/chapt09_images/ch09_img06.png)
*Figura M3.45: varianti di planning in base a complessità e livello di controllo richiesto*

![Esempio di piano operativo senza riflessione](assets/chapt09_images/ch09_img05.png)
*Figura M3.46: sequenza iniziale dei passi che l'agente può eseguire su un caso roadmap*

### Reflection e riduzione errori
Per migliorare affidabilità serve introdurre cicli di auto-valutazione. Una strategia utile è far riesaminare all'agente i propri output con criteri espliciti (accuratezza, completezza, rischio, azionabilità), poi forzare una revisione prima dell'esecuzione finale.

![Schema di riflessione e miglioramento su un sottotask](assets/chapt09_images/ch09_img07.png)
*Figura M3.47: loop di feedback interno per correggere passaggi deboli prima dell'azione*

### Memoria: continuità tra sessioni e apprendimento
Gli agenti devono mantenere stato operativo su due livelli:
- **memoria breve**: contesto della sessione corrente;
- **memoria lunga**: preferenze utente, errori passati, pattern utili, policy efficaci.

La memoria lunga consente iterazioni migliori nel tempo, ma richiede governance forte su qualità dato, privacy e aggiornamento.

![Memoria di breve e lungo periodo per sistemi agentici](assets/chapt09_images/ch09_img09.png)
*Figura M3.48: separazione tra contesto sessione e conoscenza persistente dell'agente*

### Multi-agent collaboration e pattern supervisor
Quando un solo agente diventa troppo generico, conviene specializzare: discovery, analisi, prioritizzazione, esecuzione. Un agente supervisore coordina handoff, risolve conflitti e verifica allineamento con obiettivi business.

![Pattern supervisor con agenti specializzati](assets/chapt09_images/ch09_img13.png)
*Figura M3.49: orchestrazione di più agenti per task ad alta complessità*

### Guardrail operativi per andare in produzione
Per rendere sostenibile l'adozione, fissare policy tecniche e organizzative:
1. limiti di autonomia per categoria di azione;
2. whitelist di tool e permessi minimi;
3. trigger HITL su bassa confidenza o impatto alto;
4. tracciamento completo delle decisioni dell'agente;
5. meccanismi di rollback su azioni write-enabled;
6. test regressivi frequenti su workflow critici.

### Checklist dei concetti principali
1. Scegliere il pattern di integrazione corretto per ogni processo (diretto, programmatico, backend).
2. Definire guardrail prima del go-live: sicurezza input/output, policy, soglie e fallback.
3. Valutare i modelli con benchmark pubblici e test sul dataset reale del dominio.
4. Gestire il prompting come asset versionato, con template, metriche e review periodiche.
5. Impostare un RAG con metriche su retrieval, groundedness e qualità della risposta finale.
6. Introdurre agenti in modo progressivo, con limiti di autonomia, HITL e monitoraggio continuo.

## Modulo 04: Valutare la qualità dell’output
### Scheda rapida del modulo
- **Obiettivo:** valutare la qualità dell'output AI in modo strutturato, con criteri tecnici, rischi di governance e impatto business.
- **Focus operativo:** sicurezza, privacy, bias, trasparenza e accountability come leve concrete di qualità.
- **Risultato atteso:** un framework di controllo che riduce incidenti e aumenta affidabilità, adozione e compliance.

### Qualità dell'output: oltre la sola accuratezza
La qualità di una risposta AI non coincide solo con "è corretta o no". In un contesto aziendale serve valutare almeno cinque dimensioni simultanee:

1. **Correttezza fattuale** (aderenza alle fonti e assenza di invenzioni).
2. **Rilevanza rispetto al task** (risponde davvero alla richiesta).
3. **Sicurezza** (assenza di azioni o suggerimenti dannosi).
4. **Equità** (assenza di pattern discriminatori sistematici).
5. **Comprensibilità e tracciabilità** (output interpretabile e giustificabile).

Questo approccio riduce il rischio di risposte formalmente ben scritte ma operative­mente sbagliate.

### Sicurezza dell'output su tre livelli
Per governare la qualità bisogna controllare la sicurezza su:
- **dati** (integrità e confidenzialità),
- **modello** (supply chain e dipendenze),
- **uso in produzione** (input avversariali, output non sicuri, abuso dei canali di integrazione).

![Sicurezza AI sui livelli dati, intelligenza e user experience](assets/chapt11_images/ch11_img04.png)
*Figura M4.1: le aree di sicurezza da presidiare per evitare degrado della qualità in produzione*

### Sicurezza dei dati: integrità, riservatezza, proprietà intellettuale
I principali vettori di rischio dati sono:

1. **Data poisoning:** dati alterati che degradano output e raccomandazioni.
2. **Data leakage/exfiltration:** esposizione non autorizzata di informazioni sensibili.
3. **IP exposure:** uso improprio di contenuti proprietari o coperti da licenza.

![Classificazione dei dati per livelli di confidenzialità](assets/chapt11_images/ch11_img05.png)
*Figura M4.2: classificazione dati come base per policy differenziate di accesso e protezione*

Contromisure minime:
- validazione sistematica dataset in ingresso;
- minimizzazione e anonimizzazione dove possibile;
- cifratura end-to-end e controlli RBAC;
- audit periodici su flussi dati e log di accesso.

### Sicurezza del modello: rischio supply chain
Quando si integrano componenti esterni, la qualità dell'output dipende anche dalla fiducia nel software di terze parti. La gestione corretta include:
- scansione vulnerabilità delle dipendenze;
- SBOM per inventario completo dei componenti;
- aggiornamento controllato delle librerie;
- sandboxing e policy di isolamento;
- vendor risk management con test regolari.

### Sicurezza d'uso: prompt injection e output handling
Il rischio più immediato per la qualità in ambienti aperti è il prompt injection, sia:
- **diretto** (istruzioni malevole nel prompt utente),
- **indiretto** (istruzioni malevole introdotte da fonti esterne recuperate).

![Prompt injection diretto](assets/chapt11_images/ch11_img07.png)
*Figura M4.3: istruzioni nocive inserite direttamente nella richiesta utente*

![Prompt injection indiretto da fonte esterna](assets/chapt11_images/ch11_img08.png)
*Figura M4.4: istruzioni nocive veicolate attraverso documenti o pagine recuperate*

![Esempio di input malevolo che tenta di disattivare i guardrail](assets/chapt11_images/ch11_img10.png)
*Figura M4.5: payload avversariale tipico da intercettare prima della generazione*

Pratiche essenziali:
1. validazione input e filtri semantici;
2. separazione netta tra istruzioni di sistema e contenuto utente;
3. reset di sessione per limitare accumulo di contesto manipolato;
4. output validation prima dell'esecuzione da parte di sistemi downstream.

Quando si implementano pattern per ridurre prompt avversariali e migliorare la qualità dell'output, una leva utile è costruire una Search App con controlli espliciti sull'interazione. In questo assetto si possono combinare:
- filtri contro query avversariali o poco rilevanti;
- retrieval su fonti indicizzate e controllate;
- doppia query o doppio passaggio di ricerca/risposta per verificare meglio pertinenza e aggiornamento del contenuto restituito.

![Schermata di configurazione di una Search App per grounding in Google Cloud AI Applications](assets/chapt03_images/search_app_grounding_builder_m03.png)
*Figura M4.5b: esempio di Search App configurata per grounding, filtri su query avversariali e test della qualità dell'output su fonti recuperate*

### Privacy-by-design come requisito di qualità
Un output è di qualità solo se non compromette dati personali, segreti industriali o informazioni regolamentate. Per questo la privacy va progettata dall'inizio, non aggiunta a posteriori.

![Principali rischi privacy in un sistema AI](assets/chapt11_images/ch11_img02.png)
*Figura M4.6: mappa dei punti di vulnerabilità privacy lungo la catena del valore AI*

![Principi guida della privacy-by-design](assets/chapt11_images/ch11_img03.png)
*Figura M4.7: principi operativi per incorporare protezione dati nel lifecycle*

I sette principi della privacy by design, da applicare come criteri operativi lungo tutto il ciclo di vita del sistema, sono:
- **Proattivo, non reattivo; preventivo, non correttivo:** la privacy va affrontata nelle fasi iniziali di analisi e progettazione, anticipando i rischi prima che diventino incidenti. Questo implica valutazioni d'impatto privacy, identificazione preventiva delle vulnerabilità e correzione dei punti deboli prima del rilascio.
- **Privacy come impostazione predefinita:** la configurazione standard del sistema deve proteggere i dati senza richiedere azioni aggiuntive da parte dell'utente. Anonimizzazione, minimizzazione e mascheramento dei dati sensibili devono quindi essere attivi di default.
- **Privacy incorporata nella progettazione:** i controlli privacy non vanno aggiunti a valle, ma integrati direttamente nell'architettura, nei flussi dati e nelle logiche del modello. Significa progettare fin dall'inizio limitazione del dato, uso di dati anonimizzati e meccanismi tecnici che riducano l'esposizione non necessaria.
- **Piena funzionalità:** proteggere la privacy non deve significare rinunciare al valore del sistema. L'obiettivo è una logica "positive-sum": mantenere efficacia, qualità dell'output e innovazione senza sacrificare la tutela dei dati.
- **Sicurezza end-to-end:** i dati devono essere protetti dall'acquisizione fino alla cancellazione o archiviazione finale. Servono quindi cifratura in transito e a riposo, controlli di accesso robusti e procedure di cancellazione sicura quando il dato non è più necessario.
- **Visibilità e trasparenza:** utenti, clienti e stakeholder devono poter capire come i dati vengono trattati, per quali finalità e con quali controlli. Report di utilizzo, log consultabili e spiegazioni chiare sui flussi dati rafforzano fiducia e verificabilità.
- **Rispetto della privacy dell'utente:** le persone devono mantenere controllo reale sui propri dati e sulle preferenze di utilizzo. Questo richiede dashboard semplici, opzioni di consenso e revoca, nonché possibilità di modificare in ogni momento le impostazioni privacy.

In pratica:
- selezionare modelli e fornitori con policy di retention chiare;
- evitare trasferimenti non necessari di dati sensibili;
- definire consenso, finalità e tempi di conservazione;
- documentare controlli e responsabilità.

### Bias e fairness: prevenire qualità distorta
La qualità si degrada quando il sistema produce risultati sbilanciati tra gruppi o contesti. Le fonti principali del bias sono:
- dati storici non rappresentativi,
- scelte algoritmiche non neutre,
- feedback loop che rinforzano errori passati.

![Origini del bias: dati, algoritmo, feedback loop](assets/chapt11_images/ch11_img06.png)
*Figura M4.8: le tre sorgenti da monitorare per evitare discriminazioni sistematiche*

Per rendere operativo questo controllo non basta dichiarare che il bias va monitorato: servono strumenti che aiutino il team a misurare differenze tra gruppi, analizzare errori e documentare le evidenze. Per questo è utile richiamare qui alcuni riferimenti già presenti nel corso:
- **[Google Responsible AI Docs](https://ai.google.dev/responsible/docs):** utile per impostare principi, checklist e controlli pratici quando si progettano test di fairness e sicurezza su applicazioni GenAI.
- **[Responsible AI Toolbox](https://responsibleaitoolbox.ai/):** utile per analizzare fairness, error analysis, interpretabilità e qualità del modello con un approccio più operativo in fase di validazione.
- **[Responsible AI Dashboard Tour - Notebook](https://github.com/microsoft/responsible-ai-toolbox/blob/main/notebooks/responsibleaidashboard/tabular/tour.ipynb):** utile come esempio concreto di utilizzo degli strumenti Microsoft per leggere metriche, confrontare segmenti e capire dove il modello produce effetti sbilanciati.

Un esempio concreto riportato nel model card di **DistilGPT2** su Hugging Face mostra bene come il bias possa emergere già in una semplice generazione testuale. Nell'esempio ufficiale viene usata la stessa pipeline `text-generation`, con lo stesso `seed`, cambiando solo il prompt da `The White man worked as a` a `The Black man worked as a`. Il punto rilevante non è una singola frase, ma il pattern: per il primo prompt il modello associa più spesso ruoli come **salesman**, **contractor** o **police spokesman**; per il secondo compaiono invece ruoli come **shop assistant** e **waiter**, oltre a un output che introduce una situazione di aggressione. Questo è un caso didatticamente utile perché mostra tre segnali tipici di bias:
- **associazione stereotipata tra identità e professione:** il modello non distribuisce in modo neutro i ruoli lavorativi;
- **variazione del tono narrativo:** a parità di struttura del prompt, una categoria viene associata più facilmente a contesti negativi o vulnerabili;
- **persistenza del bias nei modelli compressi:** anche una versione più leggera come DistilGPT2 eredita o riproduce distorsioni presenti nei dati e nel modello di partenza.

Dal punto di vista operativo, questo esempio serve a ricordare che i test di fairness non devono limitarsi a metriche aggregate: conviene anche costruire prompt paralleli e controllati per confrontare come il modello descrive gruppi diversi in scenari equivalenti.

Approccio di mitigazione:
1. dataset più bilanciati e aggiornati;
2. metriche fairness in validazione e monitoraggio;
3. supervisione umana su decisioni ad alto impatto;
4. alert automatici su drift di distribuzione tra segmenti.

### Trasparenza e fiducia nell'output
Per favorire adozione e uso corretto, l'output deve essere:
- **spiegabile** (perché quella risposta),
- **interpretabile** (leggibile da chi decide),
- **accountable** (chi è responsabile e come si interviene).

![Le tre componenti della trasparenza: explainability, interpretability, accountability](assets/chapt11_images/ch11_img09.png)
*Figura M4.9: struttura di trasparenza necessaria per fiducia e adozione nel business*

Un modo pratico per aumentare la **spiegabilità percepita** è usare modelli che offrono una modalità di reasoning o **Thinking** più esplicita. Esempi utili da osservare oggi sono:
- **OpenAI reasoning models**: modelli orientati al ragionamento strutturato, utili quando serve scomporre il problema in passaggi più leggibili e produrre risposte più verificabili sul piano logico.
- **Google Gemini 2.5**: Google presenta Gemini 2.5 come una famiglia di modelli con capacità di reasoning più forti, adatta a task multi-step, analisi e pianificazione.
- **Anthropic Claude con extended thinking**: Anthropic offre una modalità di ragionamento esteso che permette di dedicare più elaborazione ai problemi complessi.

Dal punto di vista progettuale, queste modalità possono aiutare la spiegabilità in almeno tre modi:
- rendono più facile chiedere al modello di **esplicitare passaggi intermedi**, criteri di confronto e ipotesi considerate;
- producono output più adatti a **review umana**, perché il team può controllare meglio coerenza, completezza e salti logici;
- aiutano a costruire interfacce in cui il modello separa **risposta finale**, **passaggi di ragionamento**, **incertezze** e **fonti o assunzioni**.

Questo però resta un approccio solo **parziale** alla spiegabilità. Il motivo è che il testo di reasoning mostrato all'utente non equivale a una vera ispezione dei meccanismi interni del modello:
- non mostra direttamente quali attivazioni, pesi o rappresentazioni interne hanno determinato l'output;
- può essere una **razionalizzazione leggibile** utile per l'utente, ma non una prova completa di ciò che il modello "ha davvero fatto" internamente;
- può aumentare fiducia e verificabilità operativa, ma non sostituisce test, audit, analisi degli errori, tracciabilità dei dati e controlli indipendenti.

La regola pratica è quindi questa: usare la modalità Thinking come supporto a **trasparenza operativa e revisione**, non come garanzia definitiva di spiegabilità tecnica del modello.

### Accountability operativa: HITL, HOTL, HOOTL
La scelta del livello di supervisione determina qualità e rischio:

1. **HITL** (Human-in-the-Loop): approvazione umana obbligatoria prima dell'azione.
2. **HOTL** (Human-on-the-Loop): monitoraggio umano con possibilità di intervento.
3. **HOOTL** (Human-out-of-the-Loop): automazione piena su casi a basso rischio e regole stabili.

La regola pratica è semplice: più alto l'impatto potenziale dell'errore, più forte deve essere la supervisione umana.

### Approccio proattivo: governance shift-left
Per evitare gestione reattiva degli incidenti, la governance va anticipata nelle prime fasi di progettazione: ideazione, dati, sviluppo, test, rilascio e monitoraggio continuo.

![Roadmap shift-left per implementare governance proattiva](assets/chapt11_images/ch11_img01.png)
*Figura M4.10: integrazione anticipata dei controlli per ridurre rischi e rework in produzione*

### KPI di qualità da monitorare nel Modulo 04
1. **Groundedness:** quota output supportati da fonti affidabili.
2. **Fedeltà al task:** aderenza ai requisiti espliciti della richiesta.
3. **Coerenza:** stabilità logica interna della risposta.
4. **Rilevanza:** pertinenza al contesto utente e al dominio.
5. **Security incident rate:** frequenza di prompt injection o output non sicuri.
6. **Fairness metrics:** differenze di qualità/esito tra gruppi o segmenti.
7. **Privacy incidents:** eventi di leakage o accesso improprio.

### Checklist dei concetti principali
1. Definire criteri di qualità multi-dimensione prima dei test di output.
2. Implementare validazione input/output e guardrail di sicurezza.
3. Applicare privacy-by-design su dati, prompt, log e integrazioni.
4. Inserire controlli fairness nel ciclo di validazione e monitoraggio.
5. Stabilire livello di oversight umano per ogni tipologia di decisione.
6. Attivare roadmap shift-left con audit periodici e miglioramento continuo.

### Link utili del modulo
| Titolo | Descrizione | Link |
| --- | --- | --- |
| Google Responsible AI (Generative AI) | Documentazione pratica per tradurre principi di fairness, sicurezza e trasparenza in checklist di progetto, test e controlli di rilascio su applicazioni GenAI. | [Google AI - Responsible AI Docs](https://ai.google.dev/responsible/docs) |
| Responsible AI Toolbox | Toolkit Microsoft con strumenti per fairness assessment, error analysis, interpretabilità e monitoraggio della qualità del modello in validazione. | [Responsible AI Toolbox](https://responsibleaitoolbox.ai/) |
| Responsible AI Dashboard Tour (Tabular) | Notebook ufficiale che mostra come usare il dashboard Microsoft per confrontare gruppi, leggere metriche di fairness e individuare aree di rischio operativo. | [Responsible AI Dashboard Tour - Notebook](https://github.com/microsoft/responsible-ai-toolbox/blob/main/notebooks/responsibleaidashboard/tabular/tour.ipynb) |
| DistilGPT2 Model Card (Hugging Face) | Model card utile per mostrare in modo immediato come emergono bias e stereotipi nella generazione testuale, con esempi riproducibili via `pipeline('text-generation')`. | [Hugging Face - distilbert/distilgpt2](https://huggingface.co/distilbert/distilgpt2) |
| OpenAI Reasoning Models | Riferimento utile per osservare come i modelli reasoning possono essere usati per scomporre problemi complessi e rendere più verificabile la logica della risposta. | [OpenAI Platform - Reasoning](https://platform.openai.com/docs/guides/reasoning) |
| Google Gemini 2.5 | Documentazione ufficiale su una famiglia di modelli con capacità di reasoning avanzato, utile per capire come strutturare task multi-step e analisi più trasparenti. | [Google AI for Developers - Gemini 2.5](https://ai.google.dev/gemini-api/docs/models#gemini-2.5) |
| Anthropic Extended Thinking | Documentazione ufficiale della modalità extended thinking di Claude, utile per comprendere quando usare più elaborazione esplicita nei task complessi. | [Anthropic Docs - Extended Thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking) |

## Modulo 05: Presidio e manutenzione nel quotidiano
### Scheda rapida del modulo
- **Obiettivo:** trasformare la governance AI in una pratica operativa continua, non in un documento statico.
- **Focus:** presidio quotidiano di rischi, processi, ruoli, metriche e aggiornamento delle policy.
- **Risultato atteso:** framework mantenibile che scala con nuovi casi d'uso e con l'evoluzione normativa.

### Presidio continuo: dal framework alla pratica
Un sistema AI resta affidabile solo se governance e manutenzione sono integrate nelle attività ordinarie di team prodotto, engineering, risk e compliance. Il punto chiave è passare da interventi reattivi a un ciclo continuo di prevenzione, monitoraggio e miglioramento.

Il framework efficace ha quattro caratteristiche:
1. **fondazione chiara** (principi etici e sponsorship dirigenziale),
2. **processi applicabili** (policy operative e checklist usabili),
3. **monitoraggio attivo** (metriche, audit, segnalazioni),
4. **capacità evolutiva** (revisioni periodiche e adattamento rapido).

![Modello di riferimento per framework di AI governance](assets/principles_ch06_images/pg_ch06_img01.jpg)
*Figura M5.1: struttura di riferimento per impostare e mantenere la governance AI nel tempo*

### Fase 1: avvio e allineamento organizzativo
Il presidio quotidiano parte da decisioni iniziali corrette:

1. **Executive buy-in:** sponsorship forte per priorità, budget e responsabilità.
2. **Team cross-funzionale:** data science, IT, legale, risk, business owner.
3. **Baseline assessment:** mappatura di use case AI, dati, controlli già esistenti.
4. **Principi guida:** fairness, trasparenza, privacy, sicurezza, accountability.

Senza questi elementi la manutenzione diventa frammentata e dipendente da singole persone.

### Fase 2: definire i componenti core di governance
Per presidiare i sistemi AI servono policy concrete su aree ad alta esposizione:

- **Data governance:** qualità, accessi, retention, permessi, tracciabilità.
- **Model governance:** standard di sviluppo, validazione, documentazione, rilascio.
- **Bias governance:** test fairness, controlli pre e post deploy, remediation.
- **Risk management:** metodologia unica per identificare, quantificare e prioritizzare i rischi.
- **Incident management:** gestione escalation, contenimento, analisi causa radice.

La regola operativa è evitare policy astratte: ogni policy deve tradursi in compiti, owner, soglie e tempi.

### Fase 3: trasformare il framework in operatività giornaliera
Un framework diventa vivo quando entra nel flusso di lavoro:

1. **Pilot su progetto reale:** applicare il framework a un caso rappresentativo.
2. **Training mirato:** ruoli diversi ricevono istruzioni diverse, non formazione generica.
3. **Template e tool:** checklist, modelli di report, playbook incidenti, dashboard.
4. **Ritmo di revisione:** checkpoint periodici con evidence oggettive.

La scalabilità nasce da processi semplici e ripetibili, non da complessità documentale.

### Presidio quotidiano del ciclo di vita AI
Nel day-by-day il team deve mantenere sotto controllo quattro fronti:

1. **Prestazioni modello:** accuratezza, robustezza, degradazione nel tempo.
2. **Rischio operativo:** errori critici, comportamenti inattesi, impatti downstream.
3. **Rischio etico/compliance:** fairness, trasparenza, privacy, audit trail.
4. **Adozione utente:** qualità percepita, fiducia, feedback e tasso di correzione manuale.

### Monitoraggio e manutenzione: regole pratiche
Per evitare derive nel tempo:

- monitorare data drift e model drift con soglie esplicite;
- validare periodicamente output su casi reali ad alto impatto;
- aggiornare dataset, prompt, regole di controllo e policy di rilascio;
- rieseguire test di regressione prima di ogni modifica significativa;
- mantenere log completi per audit e accountability.

### Governance come sistema evolutivo
La manutenzione quotidiana richiede una mentalità iterativa:
- raccogliere segnali deboli (feedback utenti, anomalie, quasi-incidenti),
- tradurli in miglioramenti prioritizzati,
- aggiornare framework, controlli e formazione,
- verificare l'efficacia delle modifiche con metriche comparabili.

Così il framework resta allineato sia alla maturità interna sia al contesto esterno in cambiamento.

### KPI essenziali del Modulo 05
1. **Copertura governance:** percentuale di progetti AI sotto policy formalizzate.
2. **Tempo di rilevazione incidenti:** velocità di individuazione anomalie.
3. **Tempo di remediation:** rapidità di correzione dopo segnalazione.
4. **Drift rate:** frequenza e severità di data/model drift.
5. **Fairness stability:** variazione delle metriche fairness nel tempo.
6. **Audit readiness:** completezza di evidenze, log e documentazione.

### Modello di governance e oversight: come strutturare il presidio
Quando l'adozione AI cresce, il presidio quotidiano richiede una struttura organizzativa esplicita, con responsabilità distribuite tra livello strategico, tattico e operativo. L'obiettivo è evitare zone grigie decisionali e rallentamenti in approvazione, remediation e audit.

Elementi indispensabili del modello di oversight:
1. **indirizzo strategico** (priorità, risk appetite, investimenti);
2. **orchestrazione tattica** (policy, standard, processi trasversali);
3. **esecuzione operativa** (controlli su dati, modelli, rilasci e monitoraggio).

![Schema di AI governance oversight su livelli strategico, tattico e operativo](assets/principles_ch07_images/pg_ch07_p01_img01.jpg)
*Figura M5.2: modello di oversight con council, owners, CoE e team AI/Data Science*

### AI Governance CoE: quando conviene attivarlo
Un Centro di Eccellenza di governance AI è utile quando i progetti diventano numerosi, eterogenei e ad alto impatto regolatorio.

Vantaggi principali:
- standardizzazione di metodi e controlli;
- riduzione rework e tempi di remediation;
- presidio centralizzato di rischio e compliance;
- supporto metodologico ai team di delivery;
- maggiore fiducia di clienti, partner e audit.

Quando partire in modalità leggera:
- organizzazione in fase iniziale di adozione AI;
- pochi casi d'uso e bassa esposizione regolatoria;
- risorse specialistiche ancora limitate.

### Componenti core di una strategia CoE
Per funzionare, il CoE deve avere mandato chiaro e strumenti pratici:

1. **Visione e perimetro:** advisory o decisionale, aree coperte, criteri di escalation.
2. **Policy e standard:** dati, sviluppo modello, validazione, fairness, sicurezza, privacy.
3. **Workflow:** processi di design review, go/no-go, monitoraggio e incident handling.
4. **Tooling:** piattaforme per testing, explainability, drift detection, reporting.
5. **Regulatory watch:** monitoraggio continuo norme e impatti operativi.
6. **Formazione diffusa:** training per tecnici, business owner, risk/legal e leadership.

### Ruoli e responsabilità del modello operativo
Un presidio robusto richiede ruoli distinti e coordinati:

- **Steering Committee:** definisce direzione, risorse e priorità.
- **CoE Lead:** governa operatività quotidiana e qualità dei processi.
- **Team cross-funzionale:** data science, IT/cyber, risk, legal/compliance, business.
- **Advisor indipendenti (opzionali):** supporto su casi ad alta complessità.

Responsabilità minime da formalizzare:
1. sviluppo/aggiornamento policy;
2. revisione progetti ad alto rischio;
3. monitoraggio KPI e indicatori rischio;
4. audit trail e evidence management;
5. gestione incidenti e lesson learned.

### RACI: rendere il presidio eseguibile
Per il mantenimento quotidiano conviene adottare una matrice RACI su attività chiave.

Esempi di attività da mappare:
- approvazione modello prima del rilascio;
- monitoraggio drift e fairness;
- gestione incidenti e comunicazioni;
- revisione periodica policy;
- aggiornamento documentazione e inventario modelli.

Principi pratici per un RACI efficace:
1. un solo **Accountable** per attività;
2. ownership chiara anche su task trasversali;
3. revisione periodica della matrice in base all'evoluzione dei processi;
4. uso operativo della matrice in CAB, review e audit.

Qui **CAB** è l'acronimo di **Change Advisory Board**: il momento o gruppo formale in cui si valutano le modifiche prima del rilascio, chiarendo chi propone il cambiamento, chi lo approva, chi deve essere consultato e chi va informato.

![Esempio di matrice RACI ad alto livello per governance AI](assets/principles_ch07_images/pg_ch07_p16_img01.jpg)
*Figura M5.3: esempio pratico di attribuzione responsabilità Responsible, Accountable, Consulted, Informed*

### Board oversight e governance ad alta direzione
Nei contesti a rischio elevato, il board deve avere visibilità strutturata sui sistemi AI, con cadenza regolare e indicatori comparabili.

Pratiche consigliate:
- review trimestrale del rischio AI (legale, operativo, reputazionale, etico);
- reporting sintetico su incidenti, near-miss e remediation;
- verifica allineamento tra strategia AI e valori aziendali;
- valutazione periodica di competenze AI nel board.

### Subcommittee e scalabilità del modello
Quando volume e complessità aumentano, è utile creare sottocomitati tematici:
- etica e impatto;
- cyber e resilienza tecnica;
- data governance e privacy;
- model risk e validazione.

Linee guida:
1. partire con 1-2 subcommittee prioritari;
2. evitare duplicazioni di mandato;
3. stabilire meccanismi di coordinamento inter-subcommittee;
4. mantenere supervisione centralizzata del chair.

### Punti operativi su Oversight e CoE
1. Definire modello di oversight su tre livelli (strategico, tattico, operativo).
2. Valutare attivazione CoE in base a maturità, rischio e scala dei casi d'uso.
3. Formalizzare ruoli, deleghe e responsabilità con RACI aggiornabile.
4. Stabilire cadenze di steering committee, review tecniche e audit.
5. Introdurre reporting board-level con KPI rischio e qualità comparabili.
6. Pianificare revisione periodica della struttura di governance e dei subcommittee.

### Assetto organizzativo avanzato: council, CoE e accountability
Per mantenere la governance efficace nel medio periodo serve un'architettura organizzativa stabile che chiarisca chi decide, chi esegue e chi controlla. L'assetto consigliato combina:

1. **AI Governance Council** per indirizzo strategico e decisioni finali su temi critici.
2. **AI Owners** per traduzione delle policy in standard tecnici e operativi.
3. **AI/Data Science Team** per esecuzione, monitoraggio e miglioramento continuo.
4. **CoE** come motore di standardizzazione, supporto metodologico e diffusione competenze.

![Modello di AI governance oversight con livelli e responsabilità](assets/principles_ch12_images/pg_ch12_img01.jpg)
*Figura M5.4: schema integrato di governance con ruoli strategici, tattici e operativi*

### Governance CoE: dalla teoria all'operatività quotidiana
Per essere realmente utile, il CoE deve produrre risultati misurabili:
- ridurre disallineamenti tra business, risk, legal e data team;
- accelerare review e approvazioni dei modelli ad alto rischio;
- uniformare controlli di qualità, fairness e sicurezza tra business unit;
- migliorare la prontezza audit con evidenze standardizzate.

Le leve operative del CoE:
1. playbook e template obbligatori per sviluppo/validazione/rilascio;
2. tassonomia rischio condivisa con funzioni di controllo;
3. libreria centralizzata di controlli e test riusabili;
4. reporting periodico su KPI governance e trend di incidenti.

### Struttura di gestione: ruoli chiave e meccanismi decisionali
Un modello maturo distingue chiaramente:

- **Steering Committee:** priorità, risorse, escalation e conflitti interfunzionali.
- **CoE Lead:** esecuzione del piano governance e presidio end-to-end dei processi.
- **Esperti cross-funzionali:** data science, cyber, compliance, risk, business domain.
- **Advisor indipendenti (quando necessari):** supporto su scenari regolatori o ad alta criticità.

Per evitare blocchi decisionali conviene definire fin da subito:
1. frequenza meeting (ordinari + straordinari per incidenti),
2. criteri di escalation,
3. soglie di rischio che attivano revisione aggiuntiva,
4. tempi massimi per approvazione/rifiuto dei cambi.

### RACI evoluto: chiarezza esecutiva nei processi critici
La matrice RACI rimane uno strumento centrale per manutenzione quotidiana, soprattutto nelle attività ad alta esposizione:
- policy update,
- review rischio progetto,
- gestione incidente,
- go-live di modelli ad alto impatto,
- audit e compliance reporting.

![Esempio di RACI per policy, risk review e incident response](assets/principles_ch12_images/pg_ch12_img02.jpg)
*Figura M5.5: assegnazione operativa di Responsible, Accountable, Consulted, Informed*

Regole pratiche da applicare:
1. un solo accountable per attività, sempre esplicitato;
2. ownership condivisa solo dove necessario e con confini chiari;
3. revisione periodica del RACI in base a crescita organizzativa;
4. integrazione del RACI nei flussi reali (CAB, incident review, audit).

### Board e leadership: presidio strategico continuativo
Quando l'AI impatta processi core, il board deve esercitare una supervisione attiva:
- ricevere update regolari su rischi, incidenti, remediation e trend;
- validare coerenza tra strategia AI, rischio accettabile e valori aziendali;
- sostenere formazione continua su AI governance per dirigenti e comitati.

La qualità del presidio dipende anche dalla composizione: competenze su rischio, sicurezza, etica e regolazione devono convivere con esperienza business e capacità di execution.

### Punti operativi su assetto organizzativo e RACI
1. Formalizzare il modello council + CoE + team operativi con mandato documentato.
2. Definire governance cadence (meeting, escalation, decision log, audit log).
3. Implementare un RACI completo per policy, review, incidenti e go-live.
4. Collegare KPI governance a obiettivi di business e rischio accettabile.
5. Attivare reporting board-level con sintesi decisionale e stato remediation.
6. Revisionare periodicamente struttura, ruoli e responsabilità in base alla maturità AI.

### AI Auditing: presidio tecnico-controllo nel ciclo di vita
La manutenzione quotidiana dei sistemi AI richiede una funzione di audit specifica, distinta dai controlli IT tradizionali. L'audit AI verifica non solo sicurezza e conformità tecnica, ma anche qualità dati, bias, robustezza, trasparenza e impatto operativo.

A differenza dell'audit IT classico, l'audit AI deve gestire modelli che evolvono nel tempo, dataset dinamici e decisioni probabilistiche. Per questo il presidio va impostato come programma continuo, non come verifica una tantum.

### Perimetro minimo di un programma di audit AI
Un programma efficace copre almeno questi ambiti:

1. **Dati:** provenienza, qualità, completezza, bias, privacy e lineage.
2. **Modelli:** performance, stabilità, explainability, comportamento anomalo.
3. **Sicurezza:** vulnerabilità specifiche AI, abuso input, hardening controlli.
4. **Governance:** ruoli, policy, evidence, processi decisionali e tracciabilità.
5. **Compliance:** allineamento a requisiti normativi e policy interne.

### Skillset essenziali dell'AI auditor
Per operare con efficacia, il team audit deve combinare:
- competenze tecniche (ML, data engineering, software lifecycle),
- competenze risk/compliance,
- capacità di analisi statistica e investigativa,
- conoscenza del dominio business dove il modello è usato.

Senza questo mix, l'audit rischia di fermarsi a checklist formali e non intercetta i rischi reali.

### Audit process: rischio, controlli, evidenze
Il flusso operativo consigliato è:

1. identificare i rischi AI specifici per caso d'uso;
2. valutare controlli esistenti (design + effectiveness);
3. mappare gap e priorità in una matrice rischio-controlli;
4. assegnare ownership e timeline di remediation;
5. verificare l'efficacia post-remediation con follow-up audit.

La severità delle verifiche deve essere proporzionale all'impatto del sistema: maggiore è il rischio potenziale, maggiore dev'essere profondità di audit e frequenza dei controlli.

### Audit committee e governance di supervisione
Il comitato audit deve avere visibilità strutturata sui sistemi AI ad alto impatto, con reporting periodico su:
- rischi aperti e trend,
- incidenti e near-miss,
- avanzamento remediation,
- stato compliance e audit readiness.

Integrare gli audit AI nel piano ordinario del comitato evita approcci emergenziali e migliora la qualità delle decisioni di investimento e priorità.

### Cicli di audit e risk assessment
La frequenza non è uguale per tutti i sistemi: va definita con criterio risk-based.

Fattori principali:
1. criticità del caso d'uso,
2. frequenza cambi modello/dati,
3. esposizione regolatoria,
4. maturità dei controlli interni,
5. capacità di monitoraggio continuo.

Nei sistemi ad alto rischio è utile combinare monitoraggio continuo con audit periodici approfonditi.

### AI readiness per pianificare governance e audit
Prima di estendere l'audit AI in modo strutturato e continuativo, è utile valutare la readiness organizzativa su quattro pilastri:
- readiness organizzativa,
- readiness valore business,
- readiness dati,
- readiness infrastruttura.

Una modalità pratica per usare AIRI è tradurre i pilastri in una tabella di assessment con dimensioni osservabili e domande di verifica:

| Pilastro | Dimensione | Assessment |
|---|---|---|
| Organisational Readiness | Management Support | Verificare se l'organizzazione ha allocato risorse concrete per iniziative AI, inclusi budget, tempo e sponsorship manageriale. |
| Organisational Readiness | AI Literacy | Verificare se i dipendenti sanno riconoscere casi d'uso AI rilevanti e se sono in grado di usare in modo consapevole soluzioni AI acquistate o sviluppate. |
| Organisational Readiness | AI Talent | Verificare se l'organizzazione possiede o può reperire le capacità necessarie per sviluppare, integrare e mantenere modelli AI. |
| Organisational Readiness | Employee Acceptance of AI | Verificare se le persone si fidano dei sistemi basati su AI e se sono disposte ad adottarli nei processi quotidiani. |
| Organisational Readiness | Experimentation Culture | Verificare se esiste una cultura di sperimentazione che permetta ai team di esplorare, testare e sviluppare use case AI. |
| Ethics and Governance Readiness | AI Governance | Verificare se esistono regole di governance adeguate per evitare danni non intenzionali verso utenti finali, clienti o soggetti impattati. |
| Ethics and Governance Readiness | AI Risk Control | Verificare se l'organizzazione classifica correttamente il livello di rischio dei sistemi AI e adatta i controlli di conseguenza. |
| Business Value Readiness | Business Use Case | Verificare se l'organizzazione ha identificato use case AI appropriati e ne ha valutato in modo credibile il valore atteso. |
| Data Readiness | Data Quality | Verificare se esistono processi per garantire qualità del dato, accuratezza, completezza e affidabilità delle informazioni raccolte. |
| Data Readiness | Reference Data | Verificare se esiste una source of truth unica, con formati dati coerenti e metadati affidabili. |
| Infrastructure Readiness | Machine Learning (ML) Infrastructure | Verificare se l'organizzazione dispone di infrastruttura ML adeguata e sufficiente, ad esempio GPU, memoria e ambienti di training e deployment. |
| Infrastructure Readiness | Data Infrastructure | Verificare se l'organizzazione usa un'infrastruttura dati appropriata, ad esempio un data lake o repository centrale, per supportare i flussi AI. |

Il modello AIRI va usato come **assessment strutturato di preparazione all'AI**, non come formula astratta. La logica è questa: si analizzano le dimensioni distribuite nei diversi pilastri, si attribuisce un punteggio alle singole aree osservate e si ricava uno **score finale** che viene poi collocato in una matrice di readiness. Il risultato serve a capire non solo "quanto" l'organizzazione sia pronta, ma **dove** sia pronta e dove invece presenti lacune.

In termini operativi, AIRI può essere letto così:
1. si raccolgono evidenze su persone, conoscenze, disponibilità ad adottare l'AI, capacità di generare valore, qualità dei dati e adeguatezza dell'infrastruttura;
2. si valuta ciascuna dimensione con un punteggio di maturità coerente;
3. si aggregano i punteggi fino a ottenere un profilo complessivo;
4. si posiziona il risultato nella matrice finale di readiness;
5. si usano i pilastri più deboli per decidere le priorità di governance, remediation e audit.

Questo rende AIRI utile soprattutto come strumento di **diagnosi organizzativa**. Se il punteggio è debole sul fronte dati, prima di intensificare l'audit conviene rafforzare qualità, lineage e controlli di accesso. Se la debolezza è organizzativa, il problema riguarda ruoli, sponsorship, competenze e processi decisionali. Se invece il profilo è più equilibrato, l'organizzazione è in una posizione migliore per introdurre audit più frequenti, controlli più profondi e reporting più formale verso management e board.

Il punto importante è che AIRI non "spiega" da solo cosa fare: offre una **vista sintetica della preparazione** e aiuta a ordinare gli interventi prima di rendere l'audit AI più esteso e sistematico.

Per rendere il framework più concreto, può essere utile anche vedere un esempio interattivo come **AIRI Sample**: aiuta a capire come i pilastri e le dimensioni possano essere presentati in un assessment pratico, leggibile anche da stakeholder non tecnici.

![AI Readiness Index (AIRI): framework a 4 pilastri e 9 dimensioni](assets/principles_ch18_images/pg_ch18_img01.jpg)
*Figura M5.6: modello AIRI per valutare capacità di adozione e presidio AI*

![Matrice di scoring AIRI per livello di maturità AI](assets/principles_ch18_images/pg_ch18_img02.jpg)
*Figura M5.7: classificazione della maturità da iniziale a competente per guidare priorità di intervento*

### Gestione findings, eccezioni e remediation
Per trasformare audit in miglioramento reale:

1. triage per gravità e impatto;
2. analisi causa radice (non solo sintomi);
3. piani correttivi con owner, scadenze e metriche;
4. comunicazione trasparente tra audit, team tecnici e management;
5. verifica post-intervento e aggiornamento dei controlli.

Le azioni più frequenti includono riequilibrio dati, miglioramento controlli qualità, rafforzamento sicurezza, introduzione strumenti di explainability e maggiore supervisione umana nei punti critici.

### Link utili del modulo
| Risorsa | Perché è utile | Link |
|---|---|---|
| AIRI Sample | Esempio interattivo utile per visualizzare come un assessment AIRI può essere presentato e discusso in modo operativo con team e stakeholder. | [AIRI Sample](https://sample.airi.sg/) |

### Checklist dei concetti principali
1. Mantenere un framework di governance vivo, con policy applicabili e ownership esplicita.
2. Presidiare il ciclo quotidiano con KPI su drift, incidenti, fairness, qualità e audit readiness.
3. Strutturare oversight su livelli strategico, tattico e operativo con RACI aggiornabile.
4. Coordinare CoE, team tecnici e funzioni di controllo con playbook e standard condivisi.
5. Attivare audit AI continuativo con pianificazione risk-based e reporting verso la direzione.
6. Chiudere ogni finding con remediation tracciata, verifica di efficacia e aggiornamento dei controlli.

## Modulo 06: Esempi pratici - Laboratori
### Scheda rapida del modulo
- **Obiettivo:** applicare in pratica i concetti dei moduli precedenti con laboratori guidati su strumenti reali.
- **Focus:** workflow operativi su Vertex AI, produttività con Copilot e tecniche di prompt engineering.
- **Risultato atteso:** capacità di impostare un flusso end-to-end dal prototipo all'uso quotidiano, con attenzione a monitoraggio e qualità.

- **Google Vertex AI:** Model Registry, Feature Engineering, Monitoring.
- **Microsoft Copilot:** Riassunti, minuting, tecniche di produttività.
- **Prompt Engineering:** Esercitazioni pratiche per il business.

### Labs
#### Catalogo laboratori e percorsi
| Titolo e link | Categoria |
| --- | --- |
| **[Generative AI Explorer - Vertex AI](https://www.skills.google/course_templates/723?catalog_rank=%7B%22rank%22%3A1%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&search_id=73609565)** | Course |
| **[Introduction to Gemini 3](https://www.skills.google/course_templates/723/labs/568844)** | Lab |
| **[Generative AI with Vertex AI: Prompt Design](https://www.skills.google/course_templates/723/labs/568845)** | Lab |
| **[Get Started with Vertex AI Studio](https://www.skills.google/course_templates/723/labs/568846)** | Lab |
| **[Intro to Grounding with Gemini in Vertex AI](https://www.skills.google/focuses/104690?catalog_rank=%7B%22rank%22%3A8%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=73609565)** | Focus |
| **[Gmail Sentiment Analysis with Gemini and Vertex AI](https://www.skills.google/focuses/118448?catalog_rank=%7B%22rank%22%3A12%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=73610087)** | Focus |
| **[Multimodal Retrieval Augmented Generation (RAG) using the Gemini API in Vertex AI](https://www.skills.google/focuses/85643?catalog_rank=%7B%22rank%22%3A19%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=73610121)** | Focus |
| **[Create a RAG Application with BigQuery](https://www.skills.google/focuses/117532?catalog_rank=%7B%22rank%22%3A1%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=75402418)** | Focus |
| **[Get started with custom search](https://docs.cloud.google.com/generative-ai-app-builder/docs/try-enterprise-search#create_a_data_store)** | Tutorial |
| **[Identify Damaged Car Parts with Vertex AutoML](https://www.skills.google/focuses/22020?catalog_rank=%7B%22rank%22%3A27%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=73610347)** | Focus |
| **[Build and Deploy an Agent with Agent Engine in Vertex AI](https://www.skills.google/focuses/104687?catalog_rank=%7B%22rank%22%3A33%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=73610391)** | Focus |
| **[Deploy and Manage Generative AI Models](https://www.skills.google/paths/1283?catalog_rank=%7B%22rank%22%3A51%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&search_id=73610456)** | Path |

#### Important Agents
| Titolo e link | Categoria |
| --- | --- |
| **[Understand Google Cloud Agents](https://www.skills.google/course_templates/1504?catalog_rank=%7B%22rank%22%3A66%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&search_id=73610516)** | Course |
| **[Enable informed decision making with a conversational agent that uses generators and data stores](https://www.skills.google/course_templates/1504/labs/599599)** | Lab |
| **[Get Started with Agent Development Kit (ADK)](https://www.skills.google/course_templates/1504/labs/599605)** | Lab |

## Bibliografia
- **The Art of AI Product Development** — **Autore:** Janna Lipenkova — **Casa editrice:** Manning Publications
- **Managing AI Projects** — **Autori:** Malini Jain Runtasewee, Adrian Gonzalez Sanchez — **Casa editrice:** O'Reilly Media, Inc.
- **Principles of AI Governance and Model Risk Management** — **Autore:** James Sayles — **Casa editrice:** Apress
- **The AI Engineer's Guide to Surviving the EU AI Act** — **Autore:** Larysa Visengeriyeva — **Casa editrice:** O'Reilly Media, Inc. — **Link:** [O'Reilly Learning](https://learning.oreilly.com/library/view/the-ai-engineers/9781098172480/)

## Nota Home
Contenuto strutturato e selezionato editorialmente dal docente, generato con assistenza AI e revisionato da un editore umano
