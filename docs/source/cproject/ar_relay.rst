.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni festive e giveaway.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_relay:

2.16 - Controllare un Altro Circuito
===========================================

Nella nostra vita quotidiana, possiamo premere l'interruttore per accendere o 
spegnere la lampada. Ma cosa succede se vuoi controllare la lampada con il Pico W, 
in modo che si spenga automaticamente dopo dieci minuti?

Un relè può aiutarti a realizzare questa idea.

Un relè è in realtà un tipo speciale di interruttore che viene controllato da un lato 
del circuito (di solito un circuito a bassa tensione) e utilizzato per controllare 
l'altro lato del circuito (di solito un circuito ad alta tensione). Questo lo rende 
pratico per modificare i nostri elettrodomestici in modo che siano controllati da un 
programma, diventando dispositivi intelligenti o persino collegabili a Internet.

.. warning::
    La modifica degli elettrodomestici comporta un grande rischio, non provarci alla leggera, fallo sotto la guida di professionisti.

* :ref:`cpn_relay`

Qui useremo solo un semplice circuito alimentato da un modulo di alimentazione per breadboard come esempio per mostrare come controllarlo utilizzando un relè.

* :ref:`cpn_power_module`

**Componenti Necessari**

In questo progetto, abbiamo bisogno dei seguenti componenti.

È sicuramente conveniente acquistare un kit completo, ecco il link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nome	
        - ELEMENTI IN QUESTO KIT
        - LINK PER L'ACQUISTO
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Puoi anche acquistarli separatamente dai link qui sotto.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - INTRODUZIONE COMPONENTE	
        - QUANTITÀ
        - LINK PER L'ACQUISTO

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Cavo Micro USB
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Diversi
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_diode`
        - 1
        - 
    *   - 7
        - :ref:`cpn_relay`
        - 1
        - |link_relay_buy|

**Cablaggio**

Prima di tutto, costruisci un circuito a bassa tensione per controllare un relè. Guidare il relè richiede una corrente elevata, quindi è necessario un transistor, e qui usiamo l'S8050.

|sch_relay_1|

|wiring_relay_1|

Qui viene utilizzato un diodo (diodo di continuità) per proteggere il circuito. Il catodo è l'estremità con la banda argentata collegata all'alimentazione, e l'anodo è collegato al transistor.

Quando l'ingresso di tensione passa da Alto (5V) a Basso (0V), il transistor passa dalla saturazione (amplificazione, saturazione e interruzione) all'interruzione, e improvvisamente non c'è modo per la corrente di fluire attraverso la bobina.

A questo punto, se questo diodo di libera circolazione non esistesse, la bobina produrrebbe una tensione autoindotta alle due estremità che è parecchie volte superiore alla tensione di alimentazione, e questa tensione, sommata alla tensione dell'alimentazione del transistor, sarebbe sufficiente per bruciarlo.

Dopo aver aggiunto il diodo, la bobina e il diodo formano istantaneamente un nuovo circuito alimentato dall'energia immagazzinata nella bobina per scaricare, evitando così che la tensione eccessiva danneggi dispositivi come i transistor sul circuito.

* :ref:`cpn_diode`    
* `Flyback Diode - Wikipedia <https://en.wikipedia.org/wiki/Flyback_diode>`_

A questo punto il programma è pronto per essere eseguito e, dopo l'esecuzione, sentirai il suono "tik tok", che è il suono della bobina del contattore all'interno del relè che si attiva e si interrompe.

Successivamente, colleghiamo le due estremità del circuito di carico rispettivamente ai pin 3 e 6 del relè.

..(Prendi come esempio il semplice circuito alimentato dal modulo di alimentazione per breadboard descritto nell'articolo precedente.)

|sch_relay_2|

|wiring_relay_2|

A questo punto, il relè sarà in grado di controllare l'accensione e lo spegnimento del circuito di carico.

**Codice**

.. note::

   * Puoi aprire il file ``2.16_relay.ino`` nel percorso ``kepler-kit-main/arduino/2.16_relay``. 
   * Oppure copia questo codice nell'**Arduino IDE**.


   * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/3be98f10-8223-49f2-8238-2acc53ebbf80/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Quando il codice viene eseguito, il relè cambierà lo stato operativo del circuito controllato ogni due secondi.
Puoi commentare manualmente una delle righe per chiarire ulteriormente la corrispondenza tra il circuito del relè e il circuito di carico.


**Approfondimenti**


Il pin 3 del relè è normalmente aperto e si attiva solo quando la bobina del contattore è in funzione; il pin 4 è normalmente chiuso e si attiva quando la bobina del contattore è energizzata. 
Il pin 1 è collegato al pin 6 ed è il terminale comune del circuito di carico.

Spostando un'estremità del circuito di carico dal pin 3 al pin 4, sarai in grado di ottenere uno stato operativo esattamente opposto.
