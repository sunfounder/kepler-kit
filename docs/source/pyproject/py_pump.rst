.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_pump:

3.6 Pompare
=======================

Le piccole pompe centrifughe sono ideali per progetti di irrigazione automatica 
delle piante.
Possono anche essere utilizzate per creare piccoli giochi d'acqua intelligenti.

Il componente di potenza è un motore elettrico, pilotato esattamente come un normale 
motore.

* :ref:`cpn_pump`
* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

.. note::

    #. Collega il tubo all'uscita del motore, immergi la pompa nell'acqua e poi accendila.
    #. Devi assicurarti che il livello dell'acqua sia sempre superiore al motore. Il funzionamento a vuoto può danneggiare il motore a causa della generazione di calore e generare rumore.
    #. Se stai annaffiando le piante, evita che il terreno venga aspirato, poiché potrebbe ostruire la pompa.
    #. Se l'acqua non esce dal tubo, potrebbe esserci dell'acqua residua nel tubo che blocca il flusso d'aria e deve essere drenata prima.

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
        - :ref:`cpn_ta6586`
        - 1
        - 
    *   - 6
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 7
        - Batteria 18650
        - 1
        -  
    *   - 8
        - Porta Batteria
        - 1
        -  
    *   - 9
        - :ref:`cpn_pump`
        - 1
        -  

**Schema Elettrico**

|sch_pump|

**Collegamenti**

.. note::

    * Poiché la pompa richiede una corrente elevata, utilizziamo un modulo caricatore Li-po per alimentare il motore per motivi di sicurezza.
    * Assicurati che il tuo modulo caricatore Li-po sia collegato come mostrato nel diagramma. In caso contrario, un cortocircuito potrebbe danneggiare la batteria e il circuito.

|wiring_pump|

**Codice**

.. note::

    * Apri il file ``3.6_pumping.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    motor1A = machine.Pin(14, machine.Pin.OUT)
    motor2A = machine.Pin(15, machine.Pin.OUT)

    while True:
        motor1A.high()
        motor2A.low()

Dopo l'esecuzione del codice, la pompa inizierà a funzionare e vedrai l'acqua uscire dal tubo allo stesso tempo.

.. note::

    * Se il motore continua a girare dopo aver cliccato sul pulsante Stop, devi resettare il pin **RUN** sul Pico W con un filo collegato a GND, e poi scollegare questo filo per eseguire nuovamente il codice.
    * Questo perché il motore sta operando con una corrente troppo elevata, il che potrebbe causare la disconnessione del Pico W dal computer.

    |wiring_run_reset|