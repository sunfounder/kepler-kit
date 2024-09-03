.. note::

    Ciao, benvenuto nella community SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni l'accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a giveaway e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_led:



2.1 - Ciao, LED! 
=======================================

Proprio come stampare "Hello, world!" è il primo passo nell'apprendimento della programmazione, usare un programma per accendere un LED è la tradizionale introduzione alla programmazione fisica.

* :ref:`cpn_led`

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
        - :ref:`cpn_resistor`
        - 1 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|

**Schema Elettrico**

|sch_led|

Il principio di questo circuito è semplice e la direzione della corrente è mostrata nella figura. Quando GP15 emette un livello alto (3,3 V), il LED si accenderà dopo la resistenza limitatrice di corrente da 220 ohm. Quando GP15 emette un livello basso (0 V), il LED si spegnerà.

**Cablaggio**

|wiring_led|

Seguiamo la direzione della corrente per costruire il circuito!

1. Qui utilizziamo il segnale elettrico dal pin GP15 della scheda Pico W per far funzionare il LED, e il circuito inizia da qui.
2. La corrente deve passare attraverso una resistenza da 220 ohm (utilizzata per proteggere il LED). Inserisci un'estremità (qualsiasi estremità) della resistenza nella stessa fila del pin GP15 della scheda Pico W (fila 20 nel mio circuito) e inserisci l'altra estremità in una fila libera della breadboard (fila 24 nel mio circuito).
3. Prendi il LED, vedrai che uno dei suoi piedini è più lungo dell'altro. Inserisci il piedino più lungo nella stessa fila dell'estremità della resistenza e collega il piedino più corto attraverso la fessura centrale della breadboard alla stessa fila.
4. Inserisci il filo di collegamento maschio-maschio (M2M) nella stessa fila del piedino corto del LED e collegalo quindi al bus di alimentazione negativo della breadboard.
5. Utilizza un jumper per collegare il bus di alimentazione negativo al pin GND di Pico W.


**Codice**

.. note::

   * Puoi aprire il file ``2.1_hello_led.ino`` nel percorso ``kepler-kit-main/arduino/2.1_hello_led``. 
   * Oppure copia questo codice nell'**Arduino IDE**.
   * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/898b8ba7-9bdf-468d-9181-ca8535e8dca6/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Dopo l'esecuzione del codice, vedrai il LED lampeggiare.

**Come Funziona?**

Qui, colleghiamo il LED al pin digitale 15, quindi dobbiamo dichiarare una variabile int chiamata ledpin all'inizio del programma e assegnarle un valore di 15.

.. code-block:: C

    const int ledPin = 15;


Ora, inizializza il pin nella funzione ``setup()``, dove devi inizializzare il pin in modalità ``OUTPUT``.

.. code-block:: C

    void setup() {
        pinMode(ledPin, OUTPUT);
    }

In ``loop()``, ``digitalWrite()`` viene utilizzato per fornire un segnale di livello alto (3,3 V) al ledpin, il che creerà una differenza di tensione tra i piedini del LED e accenderà il LED.

.. code-block:: C

    digitalWrite(ledPin, HIGH);

Se il segnale di livello viene cambiato in LOW, il segnale del ledPin tornerà a 0 V e il LED si spegnerà.

.. code-block:: C

    digitalWrite(ledPin, LOW);


È necessario un intervallo tra accensione e spegnimento per consentire 
alle persone di vedere il cambiamento, quindi utilizziamo un codice 
``delay(1000)`` per far sì che il controller non faccia nulla per 1000 ms.

.. code-block:: C

    delay(1000);   

