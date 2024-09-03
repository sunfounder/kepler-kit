.. note::

    Ciao, benvenuto nella Community SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_ultrasonic:

6.1 Misurazione della Distanza
======================================

Il modulo sensore ultrasonico funziona sul principio dei sistemi sonar e radar per determinare la distanza da un oggetto.

* :ref:`cpn_ultrasonic`

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
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|


**Schema**

|sch_ultrasonic|

**Cablaggio**

|wiring_ultrasonic|

**Codice**

.. note::

    * Apri il file ``6.1_measuring_distance.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

    TRIG = machine.Pin(17,machine.Pin.OUT)
    ECHO = machine.Pin(16,machine.Pin.IN)

    def distance():
        TRIG.low()
        time.sleep_us(2)
        TRIG.high()
        time.sleep_us(10)
        TRIG.low()
        while not ECHO.value():
            pass
        time1 = time.ticks_us()
        while ECHO.value():
            pass
        time2 = time.ticks_us()
        during = time.ticks_diff(time2,time1)
        return during * 340 / 2 / 10000

    while True:
        dis = distance()
        print ('Distance: %.2f' % dis)
        time.sleep_ms(300)

Una volta avviato il programma, la Shell stamperà la distanza del sensore ultrasonico dall'ostacolo davanti a sé.

**Come funziona?**

I sensori ultrasonici producono onde sonore ad alta frequenza (onde ultrasoniche) emesse dalla sonda trasmittente. Quando quest'onda colpisce un oggetto, viene riflessa come eco e rilevata dalla sonda ricevente. Calcolando il tempo trascorso dalla trasmissione alla ricezione, si può determinare la distanza.
Basandosi su questo principio, si può derivare la funzione ``distance()``.

.. code-block:: python

    def distance():
        TRIG.low()
        time.sleep_us(2)
        TRIG.high()
        time.sleep_us(10)
        TRIG.low()
        while not ECHO.value():
            pass
        time1 = time.ticks_us()
        while ECHO.value():
            pass
        time2 = time.ticks_us()
        during = time.ticks_diff(time2,time1)
        return during * 340 / 2 / 10000

* Le prime righe del codice sono utilizzate per trasmettere un'onda ultrasonica di 10µs.

.. code-block:: python

    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()

* Successivamente, il programma si mette in pausa e registra l'ora corrente quando l'onda ultrasonica è stata emessa.

.. code-block:: python

        while not ECHO.value():
            pass
        time1 = time.ticks_us()

* Successivamente, il programma si sospende di nuovo. Dopo che l'eco è stata ricevuta, l'ora corrente viene registrata una seconda volta.

.. code-block:: python

        while ECHO.value():
            pass
        time2 = time.ticks_us()

* Infine, basandosi sulla differenza di tempo tra le due registrazioni, la velocità del suono (340m/s) viene moltiplicata per il tempo per ottenere il doppio della distanza tra il modulo ultrasonico e l'ostacolo (cioè, un viaggio di andata e ritorno delle onde ultrasoniche dal modulo all'ostacolo). Convertendo le unità in centimetri, otteniamo il valore restituito di cui abbiamo bisogno.

.. code-block:: python

        during = time.ticks_diff(time2,time1)
        return during * 340 / 2 / 10000

Nota che il sensore ultrasonico metterà in pausa il programma quando è in funzione, il che potrebbe causare qualche rallentamento durante la scrittura di progetti complessi.
