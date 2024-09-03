.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa ai giveaway e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_irremote:


6.4 Telecomando a Infrarossi
================================

Nell'elettronica di consumo, i telecomandi sono utilizzati per controllare 
dispositivi come televisori e lettori DVD. In alcuni casi, i telecomandi 
permettono alle persone di controllare dispositivi che sono fuori dalla loro 
portata, come i condizionatori d'aria centralizzati.

Il ricevitore IR è un componente con una fotocellula sintonizzata per ricevere 
luce a infrarossi. È quasi sempre utilizzato per la rilevazione del telecomando: 
ogni televisore e lettore DVD ne ha uno nella parte anteriore per ricevere il 
segnale IR dal telecomando. All'interno del telecomando c'è un LED IR abbinato, 
che emette impulsi IR per comunicare con il televisore, accenderlo, spegnerlo o 
cambiare canale.

* :ref:`cpn_ir_receiver`

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
        - :ref:`cpn_ir_receiver`
        - 1
        - |link_receiver_buy|

**Schema Elettrico**

|sch_irrecv|

**Collegamenti**

|wiring_irrecv|

**Codice**

**Code**

    * Apri il file ``6.4_ir_remote_control.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`. 
    
    * Qui devi usare le librerie nella cartella ``ir_rx``, verifica se sono state caricate su Pico, per un tutorial dettagliato fai riferimento a :ref:`add_libraries_py`.


.. code-block:: python

    import time
    from machine import Pin, freq
    from ir_rx.print_error import print_error
    from ir_rx.nec import NEC_8

    pin_ir = Pin(17, Pin.IN)

    def decodeKeyValue(data):
        if data == 0x16:
            return "0"
        if data == 0x0C:
            return "1"
        if data == 0x18:
            return "2"
        if data == 0x5E:
            return "3"
        if data == 0x08:
            return "4"
        if data == 0x1C:
            return "5"
        if data == 0x5A:
            return "6"
        if data == 0x42:
            return "7"
        if data == 0x52:
            return "8"
        if data == 0x4A:
            return "9"
        if data == 0x09:
            return "+"
        if data == 0x15:
            return "-"
        if data == 0x7:
            return "EQ"
        if data == 0x0D:
            return "U/SD"
        if data == 0x19:
            return "CYCLE"
        if data == 0x44:
            return "PLAY/PAUSE"
        if data == 0x43:
            return "FORWARD"
        if data == 0x40:
            return "BACKWARD"
        if data == 0x45:
            return "POWER"
        if data == 0x47:
            return "MUTE"
        if data == 0x46:
            return "MODE" 
        return "ERROR"

    # User callback
    def callback(data, addr, ctrl):
        if data < 0:  # NEC protocol sends repeat codes.
            pass
        else:
            print(decodeKeyValue(data))

    ir = NEC_8(pin_ir, callback)  # Instantiate receiver
    ir.error_function(print_error)  # Show debug information

    try:
        while True:
            pass
    except KeyboardInterrupt:
        ir.close()


Il nuovo telecomando ha un pezzo di plastica all'estremità per isolare la batteria all'interno. Devi estrarre questo pezzo di plastica per alimentare il telecomando quando lo utilizzi.
Una volta che il programma è in esecuzione, quando premi il telecomando, la Shell stamperà il tasto che hai premuto.

**Come Funziona?**

Questo programma sembra leggermente complicato, ma in realtà svolge le funzioni di base del ricevitore IR con poche righe di codice.

.. code-block:: python

    import time
    from machine import Pin, freq
    from ir_rx.nec import NEC_8

    pin_ir = Pin(17, Pin.IN)

    # User callback
    def callback(data, addr, ctrl):
        if data < 0:  # NEC protocol sends repeat codes.
            pass
        else:
            print(decodeKeyValue(data))

    ir = NEC_8(pin_ir, callback)  # Instantiate receiver

Qui viene istanziato un oggetto ``ir``, che legge i segnali acquisiti dal ricevitore IR in qualsiasi momento.

Il risultato sarà registrato in ``data`` della funzione di callback.

* `Callback Function - Wikipedia <https://en.wikipedia.org/wiki/Callback_(computer_programming)>`_

Se il ricevitore IR riceve valori duplicati (ad esempio premendo un tasto senza rilasciarlo), allora data < 0 e questo dato deve essere filtrato.

Altrimenti, data sarebbe un valore utilizzabile, ma alcuni codici potrebbero non essere comprensibili, quindi viene utilizzata la funzione ``decodeKeyValue(data)`` per decodificarli.

.. code-block:: python

    def decodeKeyValue(data):
        if data == 0x16:
            return "0"
        if data == 0x0C:
            return "1"
        if data == 0x18:
            return "2"
        if data == 0x5E:
            return "3"
        if data == 0x08:
            return "4"
        if data == 0x1C:
            return "5"
        if data == 0x5A:
            return "6"
        if data == 0x42:
            return "7"
        if data == 0x52:
            return "8"
        if data == 0x4A:
            return "9"
        if data == 0x09:
            return "+"
        if data == 0x15:
            return "-"
        if data == 0x7:
            return "EQ"
        if data == 0x0D:
            return "U/SD"
        if data == 0x19:
            return "CYCLE"
        if data == 0x44:
            return "PLAY/PAUSE"
        if data == 0x43:
            return "FORWARD"
        if data == 0x40:
            return "BACKWARD"
        if data == 0x45:
            return "POWER"
        if data == 0x47:
            return "MUTE"
        if data == 0x46:
            return "MODE" 
        return "ERROR"

Se premi il tasto **1**, il ricevitore IR emette un valore come ``0x0C``, che deve essere decodificato per corrispondere al tasto specifico.

Successivamente, ci sono alcune funzioni di debug. Sono importanti, ma non sono direttamente collegate all'effetto che dobbiamo ottenere, quindi le inseriamo semplicemente nel programma.

.. code-block:: python

    from ir_rx.print_error import print_error

    ir.error_function(print_error) # Mostra informazioni di debug

Infine, utilizziamo un ciclo vuoto come programma principale. E usiamo try-except per far uscire il programma chiudendo l'oggetto ``ir``.

.. code-block:: python

    try:
        while True:
            pass
    except KeyboardInterrupt:
        ir.close()



* `Try Statement - Python Docs <https://docs.python.org/3/reference/compound_stmts.html?#the-try-statement>`_