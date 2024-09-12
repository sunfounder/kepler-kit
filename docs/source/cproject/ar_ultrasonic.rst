.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni festive e concorsi a premi.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_ultrasonic:

6.1 - Misurare la Distanza
======================================

Il modulo sensore ultrasonico funziona secondo il principio dei sistemi sonar e radar per determinare la distanza da un oggetto.

* :ref:`cpn_ultrasonic`

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
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**Schema**

|sch_ultrasonic|

**Collegamenti**

|wiring_ultrasonic|

**Codice**

.. note::

    * Puoi aprire il file ``6.1_ultrasonic.ino`` nel percorso ``kepler-kit-main/arduino/6.1_ultrasonic``. 
    * Oppure copia questo codice nell'**Arduino IDE**.

    * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/631a1663-ce45-4d46-b8f0-7d10f32097a9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Una volta avviato il programma, il Monitor Seriale mostrerà la distanza del sensore ultrasonico dall'ostacolo di fronte.

**Come funziona?**

Per quanto riguarda l'applicazione del sensore ultrasonico, possiamo verificare direttamente la sottoprocedura.

.. code-block:: arduino

    float readSensorData(){// ...}

``PING`` è attivato da un impulso HIGH di 2 o più microsecondi. (Fornisci un 
breve impulso ``LOW`` prima per garantire un impulso ``HIGH`` pulito.)

.. code-block:: arduino

    digitalWrite(trigPin, LOW); 
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH); 
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW); 

Il pin echo viene utilizzato per leggere il segnale da PING, un impulso ``HIGH`` 
la cui durata è il tempo (in microsecondi) dal momento dell'invio del ping alla 
ricezione dell'eco dell'oggetto.

.. code-block:: arduino

    microsecond=pulseIn(echoPin, HIGH);

La velocità del suono è di 340 m/s o 29 microsecondi per centimetro.

Questo valore fornisce la distanza percorsa dal ping, andata e ritorno, quindi dividiamo per 2 per ottenere la distanza dell'ostacolo.

.. code-block:: arduino

    float distance = microsecond / 29.00 / 2;  


Nota che il sensore ultrasonico metterà in pausa il programma mentre è in funzione, il che potrebbe causare qualche ritardo quando si scrivono progetti complessi.
