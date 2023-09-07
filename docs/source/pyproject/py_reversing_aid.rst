

.. _py_reversing_aid:

7.10 Einparkhilfe
======================

Dieses Projekt nutzt eine LED, einen Summer und ein Ultraschallmodul, um ein Einparkassistenzsystem zu realisieren. Es lässt sich auf ein ferngesteuertes Auto setzen, um den realen Vorgang des Einparkens in eine Garage zu simulieren.

**Benötigte Komponenten**

Für dieses Projekt werden die folgenden Komponenten benötigt.

Es ist definitiv praktisch, ein ganzes Set zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung	
        - IN DIESEM SET ENTHALTENE ARTIKEL
        - LINK
    *   - Kepler-Set	
        - 450+
        - |link_kepler_kit|

Sie können die Teile auch einzeln über die untenstehenden Links erwerben.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTE	
        - ANZAHL
        - LINK

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Micro-USB-Kabel
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Mehrere
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_transistor`
        - 1 (S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 2 (1KΩ, 220Ω)
        - |link_resistor_buy|
    *   - 7
        - Passiver :ref:`cpn_buzzer`
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

**Schaltplan**

|sch_reversing_aid|

**Verkabelung**

|wiring_reversing_aid| 

**Code**

.. note::

    * Öffnen Sie die Datei ``7.10_reversing_aid.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny und klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.
  
    * Vergessen Sie nicht, im unteren rechten Eck den Interpreter "MicroPython (Raspberry Pi Pico)" auszuwählen.

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`.

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


* Sobald das Programm läuft, wird der Ultraschallsensor kontinuierlich die Entfernung zum vor Ihnen befindlichen Hindernis messen, und Sie können den genauen Entfernungswert in der Shell sehen.
* Je nach Entfernungswert ändern die LED und der Summer die Frequenz ihres Blinkens und Piepsens und signalisieren so die Annäherung an das Hindernis.
* Im Artikel :ref:`py_ultrasonic` wurde erwähnt, dass das Programm pausiert, während der Ultraschallsensor arbeitet.
* Um die Timing von LED und Summer nicht zu beeinträchtigen, haben wir in diesem Beispiel einen separaten Thread für die Entfernungsmessung erstellt.

