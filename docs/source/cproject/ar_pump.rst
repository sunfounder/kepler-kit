.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni festive e giveaway.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_pump:

3.6 - Pompare
=======================


Le piccole pompe centrifughe sono adatte per progetti di irrigazione automatica delle piante.
Possono anche essere utilizzate per creare piccoli giochi d'acqua intelligenti.

Il componente di alimentazione è un motore elettrico, che viene azionato esattamente come un normale motore.

* :ref:`cpn_pump`
* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

.. note::

    #. Collega il tubo all'uscita del motore, immergi la pompa nell'acqua e poi accendila.
    #. Assicurati che il livello dell'acqua sia sempre superiore al motore. Il funzionamento a vuoto potrebbe danneggiare il motore a causa del calore generato e potrebbe anche provocare rumore.
    #. Se stai irrigando le piante, evita che il terreno venga aspirato, poiché potrebbe ostruire la pompa.
    #. Se l'acqua non esce dal tubo, potrebbe esserci acqua residua nel tubo che blocca il flusso d'aria e deve essere drenata prima.

**Componenti necessari**

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
        - Supporto batteria
        - 1
        -  
    *   - 9
        - :ref:`cpn_pump`
        - 1
        -  

**Schema elettrico**

|sch_pump|

**Cablaggio**

.. note::

    * Poiché la pompa richiede un'alta corrente, utilizziamo un modulo caricatore Li-po per alimentare il motore qui per motivi di sicurezza.
    * Assicurati che il tuo modulo caricatore Li-po sia collegato come mostrato nello schema. Altrimenti, un cortocircuito potrebbe danneggiare la batteria e il circuito.

|wiring_pump|

**Codice**

.. note::

   * Puoi aprire il file ``3.6_pumping.ino`` nel percorso ``kepler-kit-main/arduino/3.6_pumping``. 
   * Oppure copia questo codice nell'**Arduino IDE**.


   * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/4194feb8-92d4-4ab4-b51c-286d014af0a6/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe> 


Dopo l'esecuzione del codice, la pompa inizia a funzionare e vedrai l'acqua scorrere fuori dal tubo allo stesso tempo.


.. note::

    * Se non riesci a caricare di nuovo il codice, questa volta devi collegare il pin **RUN** del Pico W a GND con un filo per resettarlo, e poi scollega il filo per eseguire di nuovo il codice.
    * Questo perché il motore sta operando con troppa corrente, il che potrebbe causare la disconnessione del Pico W dal computer.

    |wiring_run_reset|
