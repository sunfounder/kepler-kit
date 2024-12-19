.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni festive e concorsi a premi.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _ar_temp:

2.13 - Termometro
===========================

Un termometro è un dispositivo che misura la temperatura o un gradiente di temperatura (il grado di caldo o freddo di un oggetto). 
Un termometro ha due elementi importanti: (1) un sensore di temperatura (ad esempio, il bulbo di un termometro a mercurio o il sensore pirometrico in un termometro a infrarossi) in cui avviene una variazione con un cambiamento di temperatura; 
e (2) un mezzo per convertire questa variazione in un valore numerico (ad esempio, la scala visibile su un termometro a mercurio o il display digitale su un modello a infrarossi). 
I termometri sono ampiamente utilizzati nella tecnologia e nell'industria per monitorare i processi, in meteorologia, in medicina e nella ricerca scientifica.

Un termistore è un tipo di sensore di temperatura la cui resistenza dipende fortemente dalla temperatura e si divide in due tipi: 
Coefficiente di Temperatura Negativo (NTC) e Coefficiente di Temperatura Positivo (PTC), 
anche noti come NTC e PTC. La resistenza del termistore PTC aumenta con la temperatura, mentre per l'NTC la condizione è opposta.

In questo esperimento utilizziamo un **termistore NTC** per realizzare un termometro.

* :ref:`cpn_thermistor`


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
        - :ref:`cpn_thermistor`
        - 1
        - |link_thermistor_buy|

**Schema**

|sch_temp|

In questo circuito, il resistore da 10K e il termistore sono collegati in serie e la corrente che li attraversa è la stessa. Il resistore da 10K funge da protezione e il GP28 legge il valore dopo la conversione di tensione del termistore.

Quando la temperatura aumenta, il valore di resistenza del termistore NTC diminuisce, quindi la sua tensione diminuisce, e di conseguenza il valore letto da GP28 diminuirà; se la temperatura è sufficientemente alta, la resistenza del termistore sarà vicina a 0 e il valore di GP28 sarà vicino a 0. In questo caso, il resistore da 10K svolge un ruolo protettivo, evitando che i 3,3V e il GND siano collegati insieme, provocando un cortocircuito.

Quando la temperatura diminuisce, il valore di GP28 aumenterà. Se la temperatura è abbastanza bassa, la resistenza del termistore sarà infinita, la sua tensione sarà vicina a 3,3V (il resistore da 10K è trascurabile) e il valore di GP28 sarà vicino al valore massimo di 1023.

La formula di calcolo è mostrata di seguito.

.. code-block::

  Valore Digitale = (Tensione Analogica/3,3V) * 1023



**Cablaggio**

|wiring_temp|
 
.. #. Collega i pin 3V3 e GND del Pico W al bus di alimentazione della breadboard.
.. #. Collega un terminale del termistore al pin GP28, quindi collega lo stesso terminale al bus di alimentazione positivo con una resistenza da 10K ohm.
.. #. Collega l'altro terminale del termistore al bus di alimentazione negativo.

.. note::
    * Il termistore è nero e contrassegnato con 103.
    * Gli anelli colorati del resistore da 10K ohm sono rosso, nero, nero, rosso e marrone.

**Codice**

.. note::

    * Puoi aprire il file ``2.13_thermometer.ino`` nel percorso ``kepler-kit-main/arduino/2.13_thermometer``. 
    * Oppure copia questo codice nell'**Arduino IDE**.


    * Non dimenticare di selezionare la scheda (Raspberry Pi Pico) e la porta corretta prima di cliccare sul pulsante **Upload**.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/1ae1a028-2647-4e4c-b647-0d4759f6fd03/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>
    
Dopo l'esecuzione del programma, il Monitor Seriale stamperà le temperature in gradi Celsius e Fahrenheit.

**Come funziona?**

Ogni termistore ha una resistenza normale. 
Qui è di 10k ohm, misurata a 25 gradi Celsius. 

Quando la temperatura aumenta, la resistenza del termistore diminuisce. 
Quindi i dati di tensione vengono convertiti in quantità digitali dall'adattatore A/D. 

La temperatura in gradi Celsius o Fahrenheit viene visualizzata tramite programmazione.

.. code-block:: arduino

    long a = analogRead(analogPin);

Questa linea viene utilizzata per leggere il valore del termistore. 

.. code-block:: arduino

    float tempC = beta / (log((1025.0 * 10 / a - 10) / 10) + beta / 298.0) - 273.0;
    float tempF = 1.8 * tempC + 32.0;

Questi calcoli convertono i valori del termistore in gradi Celsius e Fahrenheit.

.. note::
    Ecco la relazione tra resistenza e temperatura: 

    **RT =RN expB(1/TK – 1/TN)** 

    * RT è la resistenza del termistore NTC quando la temperatura è TK. 
    * RN è la resistenza del termistore NTC alla temperatura nominale TN. Qui, il valore numerico di RN è 10k. 
    * TK è una temperatura in Kelvin e l'unità è K. Qui, il valore numerico di TK è 273,15 + gradi Celsius. 
    * TN è una temperatura nominale in Kelvin; anche l'unità è K. Qui, il valore numerico di TN è 273,15+25.
    * E B(beta), la costante di materiale del termistore NTC, è anche chiamata indice di sensibilità termica con un valore numerico di 3950. 
    * exp è l'abbreviazione di esponenziale, e il numero base e è un numero naturale e vale circa 2,7.

    Converti questa formula TK=1/(ln(RT/RN)/B+1/TN) per ottenere la temperatura in Kelvin che sottratta di 273,15 dà la temperatura in gradi Celsius. 

    Questa relazione è una formula empirica. È accurata solo quando la temperatura e la resistenza sono entro l'intervallo efficace.

Questo codice si riferisce al plugging di Rt nella formula TK=1/(ln(RT/RN)/B+1/TN) per ottenere la temperatura in Kelvin.

