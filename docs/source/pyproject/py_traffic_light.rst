.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_traffic_light:

7.6 Ampel
=================================

Eine `Ampel <https://de.wikipedia.org/wiki/Ampel>`_ ist ein Signalgerät, das an Straßenkreuzungen, Fußgängerüberwegen und anderen Orten aufgestellt ist, um den Verkehrsfluss zu steuern.

Ampeln werden durch die `Wiener Übereinkommen über Straßenverkehrszeichen <https://de.wikipedia.org/wiki/Wiener_%C3%9Cbereinkommen_%C3%BCber_Stra%C3%9Fenverkehrszeichen>`_ standardisiert und geben den Verkehrsteilnehmern durch abwechselndes Leuchten von LEDs in drei Standardfarben das Recht auf Vorfahrt.

* **Rotes Licht**: Bei einem blinkenden roten Licht muss der Verkehr anhalten, vergleichbar mit einem Stoppschild.
* **Gelbes Licht**: Ein Warnsignal, dass das Licht bald auf Rot umschaltet. Gelbe Lichter werden in verschiedenen Ländern (Regionen) unterschiedlich interpretiert.
* **Grünes Licht**: Erlaubt es dem Verkehr, in die angezeigte Richtung zu fahren.

In diesem Projekt werden wir drei Farben von LEDs verwenden, um die Ampelphasen darzustellen, sowie eine 4-stellige 7-Segment-Anzeige, um die Dauer jeder Verkehrsphase anzuzeigen.

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Set zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM SET
        - LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Sie können die Einzelteile auch über die unten stehenden Links separat erwerben.

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
        - :ref:`cpn_resistor`
        - 7 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|
    *   - 8
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|

**Schaltplan**

|sch_traffic_light|

* Diese Schaltung basiert auf dem :ref:`py_74hc_4dig`, ergänzt durch 3 LEDs.
* Die 3 roten, gelben und grünen LEDs sind jeweils an GP7~GP9 angeschlossen.

**Verkabelung**

|wiring_traffic_light|


**Code**

.. note::

    * Öffnen Sie die Datei ``7.6_traffic_light.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny. Klicken Sie anschließend auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, im unteren rechten Eck den Interpreter "MicroPython (Raspberry Pi Pico)" auszuwählen.

    * Für detaillierte Anleitungen verweisen wir auf :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time
    from machine import Timer

    # [Green, Yellow, Red]
    lightTime=[30, 5, 30]

    # display
    SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

    sdi = machine.Pin(18,machine.Pin.OUT)
    rclk = machine.Pin(19,machine.Pin.OUT)
    srclk = machine.Pin(20,machine.Pin.OUT)

    placePin = []
    pin = [10,13,12,11]
    for i in range(4):
        placePin.append(None)
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)

    def pickDigit(digit):
        for i in range(4):
            placePin[i].value(1)
        placePin[digit].value(0)

    def clearDisplay():
        hc595_shift(0x00)

    def hc595_shift(dat):
        rclk.low()
        time.sleep_us(200)
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_us(200)
            value = 1 & (dat >> bit)
            sdi.value(value)
            time.sleep_us(200)
            srclk.high()
            time.sleep_us(200)
        time.sleep_us(200)
        rclk.high()

    def display(num):
        
        pickDigit(0)
        hc595_shift(SEGCODE[num%10])

        pickDigit(1)
        hc595_shift(SEGCODE[num%100//10])
        
        pickDigit(2)
        hc595_shift(SEGCODE[num%1000//100])
        
        pickDigit(3)
        hc595_shift(SEGCODE[num%10000//1000])    

    # led
    # 9Red, 8Yellow,7Green
    pin = [7,8,9]
    led=[]
    for i in range(3):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

    def lightup(state):
        for i in range(3):
            led[i].value(0)
        led[state].value(1)

    # timer
    counter = 0
    color_state= 0

    def time_count(ev):
        global counter, color_state
        counter -= 1
        if counter <= 0:
            color_state = (color_state+1) % 3
            counter = lightTime[color_state]
            
    tim = Timer(period=1000, mode=Timer.PERIODIC, callback=time_count)


    while True:
        display(counter)
        lightup(color_state)

Wenn der Code ausgeführt wird, leuchtet die grüne LED für 30 Sekunden, die gelbe LED für 5 Sekunden und die rote LED für 30 Sekunden.
