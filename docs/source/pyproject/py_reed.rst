.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_reed:

2.9 Sentire il Magnetismo
================================

Il tipo più comune di interruttore reed contiene una coppia di lamelle metalliche magnetizzabili e flessibili, le cui estremità sono separate da un piccolo spazio quando l'interruttore è aperto.

Un campo magnetico proveniente da un elettromagnete o da un magnete permanente farà sì che le lamelle si attraggano a vicenda, completando così un circuito elettrico.
La forza elastica delle lamelle le fa separare e aprire il circuito quando il campo magnetico cessa.

Un esempio comune di applicazione di un interruttore reed è rilevare l'apertura di una porta o finestra, per un sistema di allarme di sicurezza.

* :ref:`cpn_reed`

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
        - :ref:`cpn_resistor`
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_reed`
        - 1
        - 

**Schema Elettrico**

|sch_reed|

Di default, GP14 è basso; e diventerà alto quando il magnete è vicino all'interruttore reed.

Lo scopo del resistore da 10K è mantenere GP14 a un livello basso stabile quando non c'è un magnete nelle vicinanze.

**Collegamenti**

|wiring_reed|


**Codice**

.. note::

    * Apri il file ``2.9_feel_the_magnetism.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    reed = machine.Pin(14, machine.Pin.IN)
    while True:
        if reed.value() == 1:
            print("There are magnets here!!")
            utime.sleep(1)

Quando il codice viene eseguito, GP14 diventa alto quando un magnete è vicino all'interruttore reed, altrimenti rimane basso. Proprio come il pulsante nel capitolo :ref:`py_button`.

**Per Saperne di Più**

Questa volta, abbiamo provato un modo flessibile di utilizzare gli interruttori: richieste di interruzione, o IRQ (Interrupt Requests).

Ad esempio, stai leggendo un libro pagina per pagina, come se un programma stesse eseguendo un thread. In quel momento, qualcuno viene da te per fare una domanda e interrompe la tua lettura. Allora quella persona sta eseguendo la richiesta di interruzione: ti chiede di smettere di fare quello che stai facendo, rispondere alle sue domande e poi tornare a leggere il libro una volta finita l'interruzione.

Anche la richiesta di interruzione in MicroPython funziona allo stesso modo, consentendo a determinate operazioni di interrompere il programma principale.


.. note::

    * Apri il file ``2.9_feel_the_magnetism_irq.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    reed_switch = machine.Pin(14, machine.Pin.IN)

    def detected(pin):
        print("Magnet!")

    reed_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=detected)


Qui viene definita prima una funzione di callback ``detected(pin)``, chiamata gestore dell'interruzione. Verrà eseguita quando viene attivata una richiesta di interruzione. Successivamente, viene configurata una richiesta di interruzione nel programma principale, che contiene due parti: il ``trigger`` e il ``handler``.

In questo programma, il ``trigger`` è ``IRQ_RISING``, il che indica che il valore del pin passa da basso ad alto (cioè, pressione del pulsante).

``handler`` è ``detected``, la funzione di callback che abbiamo definito prima.

* `machine.Pin.irq - Micropython Docs <https://docs.micropython.org/en/latest/library/machine.Pin.html#machine.Pin.irq>`_