

.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_reversing_aid:

7.10 Assistenza al Parcheggio
========================================

In questo progetto utilizziamo un LED, un cicalino e un modulo a ultrasuoni per creare un sistema di assistenza al parcheggio.
Possiamo montarlo su un'auto telecomandata per simulare il processo reale di retromarcia in un garage.


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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 2(1KΩ, 220Ω)
        - |link_resistor_buy|
    *   - 7
        - Cicalino Passivo :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 8
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 9
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**Schema**

|sch_reversing_aid|


**Collegamenti**

|wiring_reversing_aid| 

**Codice**

.. note::

    * Apri il file ``7.10_reversing_aid.py`` nel percorso ``kepler-kit-main/micropython`` o copia questo codice in Thonny, poi clicca su "Esegui Script Corrente" o semplicemente premi F5 per eseguirlo.

    * Non dimenticare di selezionare l'interprete "MicroPython (Raspberry Pi Pico)" nell'angolo in basso a destra.

    * Per tutorial dettagliati, fai riferimento a :ref:`open_run_code_py`.



.. code-block:: python


    import machine
    import time
    import _thread


    buzzer = machine.Pin(15, machine.Pin.OUT)
    led = machine.Pin(14, machine.Pin.OUT)

    TRIG = machine.Pin(17,machine.Pin.OUT)
    ECHO = machine.Pin(16,machine.Pin.IN)

    dis = 100

    def distance():
        timeout=10000*5/340 
        TRIG.low()
        time.sleep_us(2)
        TRIG.high()
        time.sleep_us(10)
        TRIG.low()
        timeout_start = time.ticks_ms() # For timeout, re-read distance
        while not ECHO.value():
            waiting_time = time.ticks_ms()
            if waiting_time - timeout_start > timeout:
                return -1
        time1 = time.ticks_us()
        while ECHO.value():
            waiting_time = time.ticks_ms()
            if waiting_time - timeout_start > timeout:
                return -1
        time2 = time.ticks_us()
        during = time.ticks_diff(time2 ,time1)
        return during * 340 / 2 / 10000

    def ultrasonic_thread():
        global dis
        while True:
            dis = distance()

    _thread.start_new_thread(ultrasonic_thread, ())

    def beep():
        buzzer.value(1)
        led.value(1)
        time.sleep(0.1)
        buzzer.value(0)
        led.value(0)
        time.sleep(0.1)

    intervals = 10000000
    previousMills=time.ticks_ms()
    time.sleep(1) 

    while True:
        if dis<0:
            pass
        elif dis <= 10:
            intervals = 300
        elif dis <= 20:
            intervals =500
        elif dis <=50:
            intervals =1000
        else:
            intervals = 2000
        if dis!=-1:
            print ('Distance: %.2f' % dis)
            time.sleep_ms(100)

        
        currentMills=time.ticks_ms()
        
        if time.ticks_diff(currentMills,previousMills)>=intervals:
            beep()
            previousMills=currentMills
        
* Non appena il programma viene eseguito, il sensore a ultrasuoni leggerà continuamente la distanza dall'ostacolo di fronte a te, e sarai in grado di vedere il valore esatto della distanza sulla shell.
* Il LED e il cicalino modificheranno la frequenza di lampeggio e di beep in base al valore della distanza, indicando così l'avvicinamento dell'ostacolo.
* Nell'articolo :ref:`py_ultrasonic` è stato menzionato che quando il sensore a ultrasuoni funziona, il programma viene sospeso.
* Per evitare interferenze con il tempo di lampeggio del LED o del cicalino, in questo esempio abbiamo creato un thread separato per il rilevamento della distanza.
