.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni festive e concorsi a premi.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_water:

2.14 - Misurare il Livello dell'Acqua
========================================

|img_water_sensor|

Il sensore d'acqua è progettato per la rilevazione dell'acqua e può essere utilizzato in diversi contesti, come il rilevamento della pioggia, del livello dell'acqua o anche delle perdite di liquidi.

Misura il livello dell'acqua attraverso una serie di tracce parallele esposte che rilevano la grandezza delle gocce d'acqua o del volume d'acqua. Il volume d'acqua viene facilmente convertito in un segnale analogico, e il valore analogico di uscita può essere letto direttamente dalla scheda di controllo principale per ottenere un allarme di livello dell'acqua.

.. warning:: 
    
    Il sensore non può essere completamente immerso nell'acqua; lascia solo la parte con le dieci tracce a contatto con l'acqua. Inoltre, alimentare il sensore in un ambiente umido accelera la corrosione della sonda e ne riduce la durata, quindi è consigliabile fornire energia solo durante la lettura delle misurazioni.

* :ref:`cpn_water_level`

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
        - :ref:`cpn_water_level`
        - 1
        - 

**Schema**

|sch_water|

**Collegamenti**

|wiring_water|

**Codice**

.. note::

    * Puoi aprire il file ``2.14_feel_the_water_level.ino`` nel percorso ``kepler-kit-main/arduino/2.14_feel_the_water_level``. 
    * Oppure copia questo codice nell'**Arduino IDE**.

    * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/32ee87a1-08eb-482f-bf4c-b12b24ef05c4/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Dopo aver eseguito il programma, immergi lentamente il modulo del sensore d'acqua nell'acqua, e mentre la profondità aumenta, la shell stamperà un valore maggiore.


**Per Saperne di Più**

Esiste un modo per utilizzare il modulo di input analogico come modulo digitale.

Prima di tutto, leggi il valore del sensore d'acqua in un ambiente asciutto, registralo e usalo come valore soglia. Poi, completa la programmazione e rileggi il valore del sensore d'acqua. Quando il valore del sensore d'acqua si discosta significativamente dal valore letto in un ambiente asciutto, è esposto a un liquido. In altre parole, posizionando questo dispositivo vicino a un tubo dell'acqua, può rilevare se c'è una perdita d'acqua.


.. note::

   * Puoi aprire il file ``2.14_water_level_threshold.ino`` nel percorso ``kepler-kit-main/arduino/2.14_water_level_threshold``. 
   * Oppure copia questo codice nell'**Arduino IDE**.

    * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.

.. :raw-code:
