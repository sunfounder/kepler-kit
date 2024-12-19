.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni festive e giveaway.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_pot:

2.11 - Gira la manopola
===========================

Nei progetti precedenti, abbiamo utilizzato l'ingresso digitale sul Pico W.
Ad esempio, un pulsante può cambiare il pin da basso livello (spento) a alto livello (acceso). Questo è uno stato di lavoro binario.

Tuttavia, Pico W può ricevere un altro tipo di segnale di ingresso: l'ingresso analogico.
Può essere in qualsiasi stato da completamente chiuso a completamente aperto, e ha un intervallo di valori possibili.
L'ingresso analogico consente al microcontrollore di percepire l'intensità della luce, l'intensità del suono, la temperatura, l'umidità, ecc. del mondo fisico.

Di solito, un microcontrollore necessita di un hardware aggiuntivo per implementare l'ingresso analogico: il convertitore analogico-digitale (ADC).
Ma il Pico W ha un ADC integrato che possiamo utilizzare direttamente.

|pin_adc|

Pico W ha tre pin GPIO che possono utilizzare l'ingresso analogico: GP26, GP27, GP28. Cioè, i canali analogici 0, 1 e 2.
Inoltre, c'è un quarto canale analogico, collegato al sensore di temperatura integrato, che non verrà trattato qui.

In questo progetto, cercheremo di leggere il valore analogico del potenziometro.

* :ref:`cpn_potentiometer`

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
        - :ref:`cpn_resistor`
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_potentiometer`
        - 1
        - |link_potentiometer_buy|

**Schema elettrico**

|sch_pot|

Il potenziometro è un dispositivo analogico e quando lo si ruota in due direzioni diverse.

Collega il pin centrale del potenziometro al pin analogico GP28. Il Raspberry Pi Pico W contiene un convertitore analogico-digitale multicanale a 16 bit. Ciò significa che mappa la tensione di ingresso tra 0 e la tensione operativa (3,3V) su un valore intero compreso tra 0 e 1023, quindi il valore di GP28 varia da 0 a 1023.

La formula di calcolo è mostrata di seguito.

.. code-block::

  Valore Digitale = (Tensione Analogica/3,3V) * 1023

Quindi, programma il valore di GP28 (potenziometro) come valore PWM di GP15 (LED).  
In questo modo scoprirai che ruotando il potenziometro, la luminosità del LED cambierà contemporaneamente.

**Cablaggio**

|wiring_pot|

**Codice**

.. note::

   * Puoi aprire il file ``2.11_turn_the_knob.ino`` nel percorso ``kepler-kit-main/arduino/2.11_turn_the_knob``. 
   * Oppure copia questo codice nell'**Arduino IDE**.
   * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.

Quando il programma è in esecuzione, possiamo vedere il valore analogico attualmente letto dal pin GP28 nel Serial Monitor. 
Ruota la manopola e il valore cambierà da 0 a 1023.
Allo stesso tempo, la luminosità del LED aumenterà man mano che aumenta il valore analogico.

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b3e3927a-bd1a-4756-83f2-141d47f99b1c/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

**Come funziona?**

Per abilitare il Serial Monitor, è necessario avviare la comunicazione seriale in ``setup()`` e impostare la velocità dati a 9600.

.. code-block:: arduino
    :emphasize-lines: 3

    void setup() {
        pinMode(ledPin, OUTPUT);
        Serial.begin(9600);
    }

    
* `Serial <https://www.arduino.cc/reference/en/language/functions/communication/serial/>`_

Nella funzione loop, il valore del potenziometro viene letto, quindi il valore viene mappato da 0-1023 a 0-255 e infine il valore dopo la mappatura viene utilizzato per controllare la luminosità del LED.

.. code-block:: arduino

    void loop() {
        int sensorValue = analogRead(sensorPin);
        Serial.println(sensorValue);
        int brightness = map(sensorValue, 0, 1023, 0, 255);
        analogWrite(ledPin, brightness);
    }

* `analogRead() <https://www.arduino.cc/reference/en/language/functions/analog-io/analogread/>`_ is used to read the value of the sensorPin (potentiometer) and assigns it to the variable ``sensorValue``.

.. code-block:: arduino

    int sensorValue = analogRead(sensorPin);

* Stampa il valore di SensorValue nel Serial Monitor.

.. code-block:: arduino

    Serial.println(sensorValue);

* Qui, è necessaria la funzione `map(value, fromLow, fromHigh, toLow, toHigh) <https://www.arduino.cc/reference/en/language/functions/analog-io/analogread/>`_ poiché il valore del potenziometro letto è nell'intervallo 0-1023 e il valore di un pin PWM è nell'intervallo 0-255. Viene utilizzata per rimappare un numero da un intervallo a un altro. Cioè, un valore di fromLow verrebbe mappato su toLow, un valore di fromHigh su toHigh, i valori intermedi sui valori intermedi, ecc.

.. code-block:: arduino

    int brightness = map(sensorValue, 0, 1023, 0, 255);

* Ora possiamo utilizzare questo valore per controllare la luminosità del LED.

.. code-block:: arduino

    analogWrite(ledPin,brightness);
