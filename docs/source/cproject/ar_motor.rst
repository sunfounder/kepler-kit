.. note::

    Ciao, benvenuto nella community SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni l'accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a giveaway e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_motor:

3.5 - Piccolo Ventilatore
============================
Ora utilizziamo il TA6586 per pilotare il motore DC e farlo ruotare in senso orario e antiorario. 
Poiché il motore DC richiede una corrente relativamente alta, per motivi di sicurezza, 
qui utilizziamo un modulo di alimentazione per fornire energia al motore.

* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

**Componenti Necessari**

In questo progetto, abbiamo bisogno dei seguenti componenti.

È sicuramente conveniente acquistare un intero kit, ecco il link:

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
        - :ref:`cpn_motor`
        - 1
        - |link_motor_buy| 
    *   - 7
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 8
        - Batteria 18650
        - 1
        -  
    *   - 9
        - Portabatteria
        - 1
        - 

**Schema Elettrico**

|sch_motor|

**Cablaggio**

.. note::

    * Poiché i motori DC richiedono una corrente elevata, utilizziamo qui un modulo di caricamento Li-po per alimentare il motore per motivi di sicurezza.
    * Assicurati che il modulo di caricamento Li-po sia collegato come mostrato nello schema. In caso contrario, un cortocircuito potrebbe danneggiare la batteria e il circuito.


|wiring_motor|



**Codice**

.. note::

   * Puoi aprire il file ``3.5_small_fan.ino`` nel percorso ``kepler-kit-main/arduino/3.5_small_fan``. 
   * Oppure copia questo codice nell'**Arduino IDE**.
   * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/26d75a18-6b91-40f4-80ab-f2cdf58644ac/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Una volta che il programma è in esecuzione, il motore ruoterà avanti e indietro in un modello regolare.


.. note::

    * Se non riesci a caricare nuovamente il codice, questa volta devi collegare il pin **RUN** sul Pico W con un filo al GND per resettarlo, e poi scollegare questo filo per eseguire nuovamente il codice.
    * Questo perché il motore sta operando con troppa corrente, il che potrebbe causare la disconnessione del Pico W dal computer. 

    |wiring_run_reset|