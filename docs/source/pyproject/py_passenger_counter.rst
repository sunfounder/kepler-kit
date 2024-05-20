.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_passage_counter:

7.4 Personen Zähler
===================

In großen Einkaufszentren, Flughäfen, Bahnhöfen, Museen und anderen öffentlichen Räumen wie Ausstellungshallen ist die Erfassung der Besucherströme unerlässlich.

In Flughäfen und Bahnhöfen beispielsweise muss die Personenanzahl strikt überwacht werden, um für Sicherheit und einen reibungslosen Ablauf zu sorgen.
Auch in Einkaufszentren lässt sich so herausfinden, zu welchen Zeiten besonders viele Besucher anwesend sind und welches Umsatzpotenzial pro Besucher besteht. 
Daraus können Verbrauchsgewohnheiten analysiert und der Umsatz gesteigert werden.

Personenzähler helfen dabei, den Betrieb dieser öffentlichen Einrichtungen effizient zu organisieren.

Ein einfacher Personenzähler wird hier mit einem PIR-Sensor und einer 4-stelligen 7-Segment-Anzeige realisiert.


**Benötigte Komponenten**

Für dieses Projekt werden die folgenden Komponenten benötigt.

Ein Gesamtset ist sicherlich praktisch, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung
        - ELEMENTE IN DIESEM KIT
        - LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Die Komponenten können auch einzeln über die untenstehenden Links erworben werden.

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
        - 4(220Ω)
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
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|

**Schaltplan**

|sch_passager_counter|

* Diese Schaltung basiert auf dem :ref:`py_74hc_4dig` und wird durch ein PIR-Modul ergänzt.
* Der PIR-Sensor sendet ein etwa 2,8 Sekunden langes High-Signal aus, wenn jemand vorbeigeht.
* Das PIR-Modul hat zwei Potentiometer: eines für die Empfindlichkeit und eines für die Erfassungsreichweite. Um das PIR-Modul optimal einzustellen, sollten beide Potentiometer vollständig gegen den Uhrzeigersinn gedreht werden.

    |img_PIR_TTE|

**Verkabelung**

|wiring_passager_counter|


**Code**

.. note::

    * Öffnen Sie die Datei ``7.4_passenger_counter.py`` im Pfad ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny. Klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, den "MicroPython (Raspberry Pi Pico)"-Interpreter in der unteren rechten Ecke auszuwählen.

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time


    pir_sensor = machine.Pin(16, machine.Pin.IN)

    SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

    sdi = machine.Pin(18,machine.Pin.OUT)
    rclk = machine.Pin(19,machine.Pin.OUT)
    srclk = machine.Pin(20,machine.Pin.OUT)

    placePin = []
    pin = [10,13,12,11]
    for i in range(4):
        placePin.append(None)
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)

    count = 0


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

    def motion_detected(pin):
        global count
        count = count+1

    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)

    while True:
        #print(count)
        
        pickDigit(0)
        hc595_shift(SEGCODE[count%10])

        pickDigit(1)
        hc595_shift(SEGCODE[count%100//10])
        
        pickDigit(2)
        hc595_shift(SEGCODE[count%1000//100])
        
        pickDigit(3)
        hc595_shift(SEGCODE[count%10000//1000])


Beim Ausführen des Codes wird die Zahl auf der 4-stelligen 7-Segment-Anzeige um eins erhöht, sobald jemand vor dem PIR-Modul vorbeigeht.

