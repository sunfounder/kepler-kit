.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_relay:

2.16 Controllare un Altra Circuito
======================================

Nella nostra vita quotidiana, possiamo premere un interruttore per accendere o spegnere una lampada.
Ma cosa succede se vuoi controllare la lampada con Pico W in modo che si spenga automaticamente dopo dieci minuti?

Un relè può aiutarti a realizzare questa idea.

Un relè è in realtà un tipo speciale di interruttore controllato da un lato del circuito (di solito un circuito a bassa tensione) e utilizzato per controllare l'altro lato del circuito (di solito un circuito ad alta tensione).
Questo rende pratico modificare i nostri elettrodomestici per essere controllati da un programma, trasformandoli in dispositivi intelligenti o addirittura collegarli a Internet.

.. warning::
    La modifica degli elettrodomestici comporta un grande pericolo, non provare a farlo alla leggera, fallo solo sotto la guida di professionisti.

* :ref:`cpn_relay`

Qui utilizziamo solo un semplice circuito alimentato da un modulo di alimentazione per breadboard come esempio per mostrare come controllarlo utilizzando un relè.

* :ref:`cpn_power_module`

**Componenti Necessari**

In questo progetto, abbiamo bisogno dei seguenti componenti.

È sicuramente conveniente acquistare un kit completo, ecco il link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nome	
        - ELEMENTI IN QUESTO KIT
        - LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Puoi anche acquistarli separatamente dai link sottostanti.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENTE	
        - QUANTITÀ
        - LINK

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

**Collegamenti**

Prima di tutto, costruisci un circuito a bassa tensione per controllare un relè.
Azionare il relè richiede un'alta corrente, quindi è necessario un transistor, e qui usiamo l'S8050.

|sch_relay_1|

|wiring_relay_1|

Qui viene utilizzato un diodo (diodo di continuità) per proteggere il circuito. Il catodo è l'estremità con la fascia argentata collegata all'alimentazione, e l'anodo è collegato al transistor.

Quando l'ingresso di tensione passa da High (5V) a Low (0V), il transistor passa dalla saturazione (amplificazione, saturazione e interruzione) alla disattivazione, e improvvisamente non c'è modo che la corrente possa fluire attraverso la bobina.

A questo punto, se questo diodo di freewheeling non esiste, la bobina produrrà un potenziale elettrico autoindotto a entrambe le estremità che è diverse volte superiore alla tensione di alimentazione, e questa tensione sommata a quella di alimentazione del transistor è sufficiente per bruciarlo.

Dopo aver aggiunto il diodo, la bobina e il diodo formano istantaneamente un nuovo circuito alimentato dall'energia immagazzinata nella bobina per scaricare, evitando così che la tensione eccessiva danneggi dispositivi come i transistor nel circuito.

* :ref:`cpn_diode`    
* `Flyback Diode - Wikipedia <https://en.wikipedia.org/wiki/Flyback_diode>`_

A questo punto il programma è pronto per essere eseguito, e dopo l'esecuzione sentirai il suono "tik tok", che è il suono della bobina del contattore all'interno del relè che si attiva e si disattiva.

Quindi colleghiamo i due estremi del circuito di carico rispettivamente ai pin 3 e 6 del relè.

..(Prendi come esempio il semplice circuito alimentato dal modulo di alimentazione del breadboard descritto nell'articolo precedente.)

|sch_relay_2|

|wiring_relay_2|

A questo punto, il relè sarà in grado di controllare l'accensione e lo spegnimento del circuito di carico.

**Codice**

.. note::

    * Apri il file ``2.16_control_another_circuit.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    
    relay = machine.Pin(15, machine.Pin.OUT)
    while True:
        relay.value(1)
        utime.sleep(2)
        relay.value(0)
        utime.sleep(2)

Quando il codice viene eseguito, il relè cambierà lo stato operativo del circuito controllato ogni due secondi.
Puoi commentare manualmente una delle righe per chiarire ulteriormente la corrispondenza tra il circuito del relè e il circuito di carico.


**Per Saperne di Più**

Il pin 3 del relè è normalmente aperto e si accende solo quando la bobina del contattore è in funzione; il pin 4 è normalmente chiuso e si accende quando la bobina del contattore è energizzata.
Il pin 1 è collegato al pin 6 ed è il terminale comune del circuito di carico.

Cambiando un'estremità del circuito di carico dal pin 3 al pin 4, sarai in grado di ottenere uno stato operativo esattamente opposto.
