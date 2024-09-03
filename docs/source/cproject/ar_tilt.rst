.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni festive e concorsi a premi.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_tilt:

2.6 - Inclinazione!
==========================

|img_tilt|

L'interruttore a inclinazione è un dispositivo a 2 pin con una sfera di metallo al centro. Quando lo posizioni in posizione verticale, i 2 pin sono collegati tra loro; quando inclini l'interruttore, i 2 pin si scollegano.


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
        - :ref:`cpn_resistor`
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_tilt`
        - 1
        - 

**Schema**

|sch_tilt|

Quando lo posizioni in posizione verticale, GP14 sarà alto; dopo averlo inclinato, GP14 sarà basso.

Lo scopo del resistore da 10K è mantenere GP14 in uno stato stabile e basso quando l'interruttore a inclinazione è in posizione inclinata.

* :ref:`cpn_tilt`

**Cablaggio**

|wiring_tilt|

**Codice**

.. note::

   * Puoi aprire il file ``2.6_tilt_it.ino`` nel percorso ``kepler-kit-main/arduino/2.4_colorful_light``. 
   * Oppure copia questo codice nell'**Arduino IDE**.


    * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.



.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/0421b002-a697-4f22-a965-0e62e8dc3abf/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

    


Dopo l'esecuzione del programma, quando inclini la breadboard (interruttore a inclinazione), apparirà nel terminale "The switch works!".
