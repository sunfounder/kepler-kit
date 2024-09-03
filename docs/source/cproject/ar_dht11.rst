.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_dht11:

6.2 - Temperatura e Umidità
=======================================

L'umidità e la temperatura sono strettamente correlate, sia come grandezze fisiche sia nella vita quotidiana delle persone.
La temperatura e l'umidità dell'ambiente umano influiscono direttamente sulla funzione di termoregolazione e sull'effetto di dissipazione del calore del corpo umano.
Questi fattori, a loro volta, influenzano l'attività mentale e lo stato d'animo, incidendo sull'efficienza nello studio e nel lavoro.

La temperatura è una delle sette grandezze fisiche fondamentali del Sistema Internazionale di Unità, utilizzata per misurare il grado di calore o freddo di un oggetto.
Il Celsius è una delle scale di temperatura più utilizzate al mondo, espressa con il simbolo "℃".

L'umidità è la concentrazione di vapore acqueo presente nell'aria.
Nella vita quotidiana si utilizza comunemente l'umidità relativa dell'aria, espressa in %RH. L'umidità relativa è strettamente legata alla temperatura.
Per un determinato volume di gas sigillato, più alta è la temperatura, più bassa sarà l'umidità relativa, e viceversa.

|img_Dht11|

In questo kit è incluso un sensore digitale di base per la temperatura e l'umidità, il **DHT11**.
Utilizza un sensore di umidità capacitivo e un termistore per misurare l'aria circostante e restituisce un segnale digitale sui pin dei dati (non sono richiesti pin di ingresso analogico).

* :ref:`cpn_dht11`

**Componenti Necessari**

In questo progetto, ci servono i seguenti componenti.

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
        - :ref:`cpn_dht11`
        - 1
        - |link_dht22_buy|

**Schema Elettrico**

|sch_dht11|

**Cablaggio**

|wiring_dht11|

**Codice**

.. note::

    * Puoi aprire il file ``6.2_dht11.ino`` nel percorso ``kepler-kit-main/arduino/6.2_dht11``.
    * Oppure copia questo codice nell'**Arduino IDE**.
    * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.
    * Qui viene utilizzata la libreria ``SimpleDHT``. Consulta :ref:`add_libraries_ar` per aggiungerla all'IDE di Arduino.




.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b9e96e99-59d4-48ca-b41f-c03577acfb8f/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Dopo l'esecuzione del codice, vedrai il Serial Monitor stampare continuamente la temperatura e l'umidità, e man mano che il programma si stabilizza, questi due valori diventeranno sempre più precisi.

**Come funziona?**

Inizializza l'oggetto DHT11. Questo dispositivo richiede solo un ingresso digitale per essere utilizzato.

.. code-block:: arduino

    int pinDHT11 = 16;
    SimpleDHT11 dht11(pinDHT11);

Legge la temperatura e l'umidità correnti, che vengono memorizzate nelle variabili ``temperature`` e ``humidity``. ``err`` viene utilizzato per determinare la validità dei dati.

.. code-block:: arduino

    byte temperature = 0;
    byte humidity = 0;
    int err = dht11.read(&temperature, &humidity, NULL);

Filtra i dati non validi.

.. code-block:: arduino

    if (err != SimpleDHTErrSuccess) {
        Serial.print("Read DHT11 failed, err="); 
        Serial.print(SimpleDHTErrCode(err));
        Serial.print(","); 
        Serial.println(SimpleDHTErrDuration(err)); 
        delay(1000);
        return;
    }    

Stampa la temperatura e l'umidità.

.. code-block:: arduino

    Serial.print((int)temperature); 
    Serial.print(" *C, "); 
    Serial.print((int)humidity); 
    Serial.println(" H");

Infine, il tasso di campionamento del DHT11 è di 1Hz, quindi è necessario un ``delay(1500)`` nel ciclo.

.. code-block:: arduino

    delay(1500);
