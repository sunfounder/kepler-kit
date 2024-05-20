.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_rgb:

2.4 Farbenfrohes Licht
==============================================

Wie wir wissen, kann Licht überlagert werden. Zum Beispiel ergibt die Kombination von blauem und grünem Licht Zyanlicht, während rotes und grünes Licht Gelblicht erzeugen. Dieses Prinzip wird als "Additive Farbmischung" bezeichnet.

* `Additive Farbe – Wikipedia <https://de.wikipedia.org/wiki/Additive_Farbmischung>`_

Basierend auf dieser Methode können wir die drei Grundfarben verwenden, um sichtbares Licht jeder beliebigen Farbe in verschiedenen Verhältnissen zu mischen. Beispielsweise kann Orange durch mehr Rot und weniger Grün erzeugt werden.

In diesem Kapitel werden wir die Geheimnisse der additiven Farbmischung mit einer RGB-LED erkunden!

Eine RGB-LED entspricht im Grunde einer Kapselung von roten, grünen und blauen LEDs unter einer einzigen Lampenabdeckung. Diese drei LEDs teilen sich einen gemeinsamen Kathodenpin. Da jedem Anodenpin ein elektrisches Signal zugeführt wird, kann das Licht der entsprechenden Farbe dargestellt werden. Durch die Änderung der Signalintensität jeder Anode können vielfältige Farben erzeugt werden.

* :ref:`cpn_rgb`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Ein vollständiges Set ist definitiv praktisch. Hier ist der Link dazu:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM SET
        - LINK
    *   - Kepler Kit
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
        - :ref:`cpn_resistor`
        - 3(1-330Ω, 2-220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|

**Schaltplan**

|sch_rgb|

Die PWM-Pins GP13, GP14 und GP15 steuern jeweils die Rot-, Grün- und Blau-Pins der RGB-LED. Der gemeinsame Kathodenpin wird mit GND verbunden. So kann die RGB-LED durch Überlagerung von Licht mit verschiedenen PWM-Werten auf diesen Pins eine bestimmte Farbe anzeigen.


**Verdrahtung**

|img_rgb_pin|

Die RGB-LED hat 4 Pins: Der längste Pin ist der gemeinsame Kathodenpin, der normalerweise mit GND verbunden ist; der linke Pin neben dem längsten ist Rot; die beiden Pins rechts davon sind Grün und Blau.


|wiring_rgb|


**Code**



.. note::

    * Öffnen Sie die Datei ``2.4_colorful_light.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny. Klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, im unteren rechten Bereich auf den "MicroPython (Raspberry Pi Pico)"-Interpreter zu klicken. 

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    red = machine.PWM(machine.Pin(13))
    green = machine.PWM(machine.Pin(14))
    blue = machine.PWM(machine.Pin(15))
    red.freq(1000)
    green.freq(1000)
    blue.freq(1000)

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def color_to_duty(rgb_value):
        rgb_value = int(interval_mapping(rgb_value,0,255,0,65535))
        return rgb_value

    def color_set(red_value,green_value,blue_value):
        red.duty_u16(color_to_duty(red_value))
        green.duty_u16(color_to_duty(green_value))
        blue.duty_u16(color_to_duty(blue_value))

    color_set(255,128,0)

Hier können wir in einer Zeichensoftware (wie etwa Paint) unsere Lieblingsfarbe auswählen und sie mit der RGB-LED anzeigen.

|img_take_color|

Tragen Sie den RGB-Wert in ``color_set()`` ein, um die gewünschten Farben mit der RGB-LED darzustellen.


**Wie funktioniert es?**

Um die drei Grundfarben gemeinsam nutzen zu können, haben wir eine ``color_set()`` Funktion definiert.

Aktuell verwenden Pixel in Computerhardware meist eine 24-Bit-Darstellung. Jede Grundfarbe wird in 8 Bit unterteilt, und der Farbwertbereich liegt zwischen 0 und 255. Es gibt 256 mögliche Kombinationen für jede der drei Grundfarben (vergessen Sie nicht, 0 zu zählen!), also 256 x 256 x 256 = 16.777.216 Farben.
Die ``color_set()`` Funktion verwendet ebenfalls die 24-Bit-Notation, um die Farbauswahl zu vereinfachen.

Da der Wertebereich von ``duty_u16()`` 0~65535 beträgt (anstelle von 0 bis 255), wenn die Ausgangssignale über PWM zur RGB-LED gesendet werden, haben wir die Funktionen ``color_to_duty()`` und ``interval_mapping()`` definiert, um die Farbwerte auf die Tastverhältniswerte abzubilden.
