.. note::

    Ciao, benvenuto nella Community di Appassionati di Raspberry Pi & Arduino & ESP32 di SunFounder su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa ai giveaway e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_dht11:

6.2 Temperatura - Umidità
=======================================

Temperatura e umidità sono strettamente correlate, sia come grandezze fisiche che nella vita quotidiana.
La temperatura e l'umidità dell'ambiente in cui viviamo influenzano direttamente la funzione termoregolatrice e l'effetto del trasferimento di calore del nostro corpo.
Questi fattori influenzano ulteriormente l'attività mentale e lo stato d'animo, condizionando così l'efficienza nello studio e nel lavoro.

La temperatura è una delle sette grandezze fisiche fondamentali nel Sistema Internazionale di Unità, utilizzata per misurare il grado di caldo e freddo di un oggetto.
Il grado Celsius è una delle scale di temperatura più utilizzate al mondo, espresso dal simbolo "℃".

L'umidità è la concentrazione di vapore acqueo presente nell'aria.
L'umidità relativa dell'aria è comunemente usata nella vita quotidiana ed è espressa in %RH. L'umidità relativa è strettamente correlata alla temperatura.
Per un certo volume di gas sigillato, maggiore è la temperatura, minore è l'umidità relativa, e viceversa, minore è la temperatura, maggiore è l'umidità relativa.

|img_Dht11|

In questo kit è incluso un sensore digitale di base per la temperatura e l'umidità, il **DHT11**.
Utilizza un sensore di umidità capacitivo e un termistore per misurare l'aria circostante e produce un segnale digitale sui pin dati (non sono richiesti pin di ingresso analogici).

* :ref:`cpn_dht11`

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
        - :ref:`cpn_dht11`
        - 1
        - |link_dht22_buy|

**Schema**

|sch_dht11|

**Cablaggio**

|wiring_dht11|

**Codice**

.. note::

    * Apri il file ``6.2_temperature_humidity.py`` nel percorso ``kepler-kit-main/micropython`` oppure copia questo codice in Thonny, quindi clicca su "Run Current Script" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`. 
    
    * Qui è necessario utilizzare la libreria chiamata ``dht.py``, verifica se è stata caricata su Pico W; per un tutorial dettagliato, fai riferimento a :ref:`add_libraries_py`.

.. code-block:: python

    from machine import Pin
    import utime as time
    from dht import DHT11, InvalidPulseCount

    pin = Pin(16, Pin.IN, Pin)
    sensor = DHT11(pin)
    time.sleep(5)  # ritardo iniziale

    while True:
        try:
            sensor.measure()
            string = "Temperature:{}\nHumidity: {}".format(sensor.temperature, sensor.humidity)
            print(string)
            time.sleep(4)

        except InvalidPulseCount as e:
            print('Bad pulse count - retrying ...')


Dopo l'esecuzione del codice, vedrai la Shell stampare continuamente la temperatura e l'umidità e, man mano che il programma continua a funzionare, questi due valori diventeranno sempre più precisi.

**Come funziona?**

Nella libreria dht, abbiamo integrato la funzionalità rilevante nella classe ``DHT11``.

.. code-block:: python

    from dht import DHT11, InvalidPulseCount

Inizializza l'oggetto ``DHT11``. Questo dispositivo richiede solo un ingresso digitale per essere utilizzato.

.. code-block:: python

    pin = Pin(16, Pin.IN)
    sensor = DHT11(pin)

Usa ``sensor.measure()`` per leggere la temperatura e l'umidità correnti, che verranno memorizzate in ``sensor.temperature``, ``sensor.humidity``.
Questi dati vengono poi stampati.
Infine, poiché la frequenza di campionamento del DHT11 è di 1Hz, è necessario un ``time.sleep(1)`` nel loop.

.. code-block:: python

    while True:
        try:
            sensor.measure()
            string = "Temperature:{}\nHumidity: {}".format(sensor.temperature, sensor.humidity)
            print(string)
            time.sleep(4)

        except InvalidPulseCount as e:
            print('Bad pulse count - retrying ...')
