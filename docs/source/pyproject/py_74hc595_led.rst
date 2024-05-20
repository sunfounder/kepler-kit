.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_74hc_led:

5.1 Mikrochip - 74HC595
========================

Ein integrierter Schaltkreis (integrated circuit, kurz IC) ist eine Art Miniatur-Elektronikbauelement oder -komponente, das in Schaltkreisen durch das Kürzel "IC" dargestellt wird.

Mit Hilfe eines speziellen Verfahrens werden Transistoren, Widerstände, Kondensatoren, Spulen und andere für einen Schaltkreis erforderliche Bauelemente und Verbindungen auf einem oder mehreren kleinen Halbleiter-Wafern oder dielektrischen Substraten angefertigt. Anschließend werden diese in ein Gehäuse eingebettet und ergeben somit eine Mikrostruktur mit den erforderlichen Schaltkreisfunktionen. Alle Bauteile sind als eine Einheit strukturiert, was einen großen Schritt in Richtung Miniaturisierung, geringem Stromverbrauch, Intelligenz und hoher Zuverlässigkeit von elektronischen Bauelementen bedeutet.

Die Erfinder der integrierten Schaltkreise sind Jack Kilby (integrierte Schaltkreise auf Germaniumbasis (Ge)) und Robert Norton Noyce (integrierte Schaltkreise auf Siliziumbasis (Si)).

Dieses Kit enthält einen IC, den 74HC595, der die Nutzung von GPIO-Pins erheblich reduziert. Konkret kann er 8 Pins für die digitale Signalausgabe ersetzen, indem ein 8-Bit-Binärzahl geschrieben wird.

* `Binärzahl – Wikipedia <https://de.wikipedia.org/wiki/Bin%C3%A4rzahl>`_

* :ref:`74HC595`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein komplettes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung
        - KOMPONENTEN IN DIESEM KIT
        - LINK
    *   - Kepler-Kit
        - 450+
        - |link_kepler_kit|

Sie können die Komponenten auch einzeln über die untenstehenden Links erwerben.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTE
        - MENGE
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
        - 8 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 8
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Schaltplan**

|sch_74hc_led|

* Wenn MR (Pin 10) auf hohem und OE (Pin 13) auf niedrigem Pegel ist, wird das Daten in der aufsteigenden Flanke von SHcp eingegeben und durch die aufsteigende Flanke von SHcp ins Speicherregister übertragen.
* Sind die beiden Taktgeber verbunden, ist das Schieberegister immer einen Puls vor dem Speicherregister.
* Im Speicherregister gibt es einen seriellen Eingangspin (Ds), einen seriellen Ausgangspin (Q) und eine asynchrone Zurücksetztaste (Low-Pegel).
* Das Speicherregister gibt einen Bus mit einem parallelen 8-Bit und in drei Zuständen aus.
* Ist OE aktiviert (Low-Pegel), werden die Daten im Speicherregister auf den Bus (Q0 ~ Q7) ausgegeben.

**Verkabelung**

.. Der 74HC595 ist ein IC mit 16 Pins und einer halbkreisförmigen Kerbe auf einer Seite (meist die linke Seite des Etiketts). Mit der Kerbe nach oben sind seine Pins im folgenden Diagramm dargestellt.

.. Beziehen Sie sich auf die untenstehende Abbildung, um den Schaltkreis aufzubauen.

|wiring_74hc_led|

.. 1. Verbinden Sie 3V3 und GND des Pico W mit der Stromschiene des Breadboards.
.. #. Setzen Sie den 74HC595 quer über die mittlere Lücke in das Breadboard.
.. #. Verbinden Sie den GP0-Pin des Pico W mit dem DS-Pin (Pin 14) des 74HC595 mit einem Jumperkabel.
.. #. Verbinden Sie den GP1-Pin des Pico W mit dem STcp-Pin (Pin 12) des 74HC595.
.. #. Verbinden Sie den GP2-Pin des Pico W mit dem SHcp-Pin (Pin 11) des 74HC595.
.. #. Verbinden Sie den VCC-Pin (Pin 16) und den MR-Pin (Pin 10) am 74HC595 mit der positiven Stromschiene.
.. #. Verbinden Sie den GND-Pin (Pin 8) und den CE-Pin (Pin 13) am 74HC595 mit der negativen Stromschiene.
.. #. Setzen Sie 8 LEDs auf das Breadboard, und deren Anoden sind jeweils mit den Pins Q0~Q1 (15, 1, 2, 3, 4, 5, 6, 7) des 74HC595 verbunden.
.. #. Verbinden Sie die Kathoden der LEDs über einen 220Ω-Widerstand in Reihe mit der negativen Stromschiene.

**Code**

.. note::

    * Öffnen Sie die Datei ``5.1_microchip_74hc595.py`` im Pfad ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny und klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.
    
    * Vergessen Sie nicht, im rechten unteren Eck den Interpreter "MicroPython (Raspberry Pi Pico)" auszuwählen.
    
    * Für detaillierte Informationen über die Funktionsweise des Codes und die zu verwendenden Bibliotheken, verweisen wir auf den Kommentarbereich im Code.

.. code-block:: python

    import machine
    import time

    sdi = machine.Pin(0,machine.Pin.OUT)
    rclk = machine.Pin(1,machine.Pin.OUT)
    srclk = machine.Pin(2,machine.Pin.OUT)

    def hc595_shift(dat): 
        rclk.low()
        time.sleep_ms(5)
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_ms(5)
            value = 1 & (dat >> bit)
            sdi.value(value)
            time.sleep_ms(5)
            srclk.high()
            time.sleep_ms(5)
        time.sleep_ms(5)
        rclk.high()
        time.sleep_ms(5)

    num = 0

    for i in range(16):
        if i < 8:
            num = (num<<1) + 1
        elif i>=8:
            num = (num & 0b01111111)<<1
        hc595_shift(num)
        print("{:0>8b}".format(num))
        time.sleep_ms(200)


Wenn das Programm läuft, wird ``num`` als achtbitige Binärzahl in den 74HC595-Chip geschrieben, um das Ein- und Ausschalten der 8 LEDs zu steuern.
Den aktuellen Wert von ``num`` können wir im Shell-Fenster einsehen.

**Wie funktioniert es?**

Die Funktion ``hc595_shift()`` bewirkt, dass der 74HC595 acht digitale Signale ausgibt. Dabei wird das letzte Bit der Binärzahl an Q0 und das erste Bit an Q7 ausgegeben. Mit anderen Worten: Schreibt man die Binärzahl „00000001“, so gibt Q0 ein hohes Signal aus, während Q1 bis Q7 ein niedriges Signal ausgeben.
