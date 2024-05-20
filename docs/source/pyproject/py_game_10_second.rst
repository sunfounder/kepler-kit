.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_10_second:

7.5 SPIEL - 10 Sekunden
=======================

Um Ihre Konzentration auf die Probe zu stellen, bauen Sie mit mir ein Spielgerät. Kreieren Sie einen Zauberstab, indem Sie den Kipp-Schalter mit einem Stab verbinden. Wenn Sie den Zauberstab schütteln, beginnt die 4-stellige 7-Segment-Anzeige mit dem Zählen. Schütteln Sie ihn erneut, stoppt das Zählen. Um zu gewinnen, muss der angezeigte Zählerstand bei **10.00** stehen bleiben. Spielen Sie das Spiel mit Ihren Freunden, um herauszufinden, wer der Zeitmagier ist.

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist natürlich praktisch, ein komplettes Set zu kaufen. Hier ist der Link dazu:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Sie können die Teile auch separat unter den folgenden Links erwerben.

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
        - 5(4-220Ω, 1-10KΩ)
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
        - :ref:`cpn_tilt`
        - 1
        - 

**Schaltplan**

|sch_10_second|

* Diese Schaltung basiert auf :ref:`py_74hc_4dig`, ergänzt durch einen Kipp-Schalter.
* GP16 ist hoch, wenn der Kipp-Schalter aufrecht ist; niedrig, wenn gekippt.

**Verkabelung**

|wiring_game_10_second|


**Code**

.. note::

    * Öffnen Sie die Datei ``7.5_game_10_second.py`` im Pfad ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny. Klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, den "MicroPython (Raspberry Pi Pico)"-Interpreter in der unteren rechten Ecke auszuwählen.

    * Für detaillierte Anleitungen verweisen wir auf :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

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
        #time.sleep_us(200)
        

    def display(num):
        
        pickDigit(0)
        hc595_shift(SEGCODE[num%10])

        pickDigit(1)
        hc595_shift(SEGCODE[num%100//10])
        
        pickDigit(2)
        hc595_shift(SEGCODE[num%1000//100]+0x80)
        
        pickDigit(3)
        hc595_shift(SEGCODE[num%10000//1000])    


    tilt_switch = machine.Pin(16,machine.Pin.IN)

    count_flag = False

    def shake(pin):
        global timeStart,count_flag
        count_flag = not count_flag
        if count_flag == True:
            timeStart = time.ticks_ms()

    tilt_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=shake)


    count = 0
    while True:
        if count_flag == True:
            count = int((time.ticks_ms()-timeStart)/10)
        display(count)

Die 4-stellige 7-Segment-Anzeige beginnt mit dem Zählen, sobald Sie den Zauberstab schütteln, und stoppt, wenn Sie ihn erneut schütteln.
Sie gewinnen, wenn es Ihnen gelingt, den angezeigten Zählstand bei 10,00 zu halten. Das Spiel wird mit einem weiteren Schütteln fortgesetzt.
