.. _py_fade:

2.3 Abklingende LED
========================

Bislang haben wir lediglich zwei Arten von Ausgangssignalen verwendet: hohes und niedriges Signalniveau, auch als EIN und AUS bezeichnet. Das nennen wir digitalen Ausgang.
In der Praxis arbeiten jedoch viele Geräte nicht ausschließlich mit diesen zwei Zuständen, sondern benötigen differenziertere Steuerungen, wie etwa die Geschwindigkeitsregelung eines Motors oder die Helligkeitsanpassung einer Schreibtischlampe.
Früher wurden dafür Schieberegler zur Widerstandseinstellung genutzt, was allerdings als unzuverlässig und ineffizient gilt.
Deshalb hat sich die Pulsweitenmodulation (PWM) als praktikable Lösung für solche komplexen Anforderungen etabliert.

Ein Puls ist im Kontext digitaler Ausgänge ein Signal, das sowohl ein hohes als auch ein niedriges Niveau enthält. Die Breite dieser Pulse kann durch Veränderung der Schaltfrequenz zwischen EIN und AUS angepasst werden.

Innerhalb einer kurzen Zeitspanne – etwa 20 Millisekunden, die der visuellen Speicherzeit der meisten Menschen entspricht – lässt sich eine LED ein- und wieder ausschalten, ohne dass uns das Auge den Wechsel als solchen wahrnimmt. Allerdings erscheint die Helligkeit der LED dann etwas reduziert.
Während dieser Phase gilt: Je länger die LED leuchtet, desto heller erscheint sie.
Mit anderen Worten, je breiter der Puls im gegebenen Zyklus ist, desto größer ist die vom Mikrocontroller ausgegebene elektrische Signalstärke.
Das ist der Mechanismus, mit dem PWM die Helligkeit der LED (oder die Geschwindigkeit des Motors) steuert.

* `Pulsweitenmodulation – Wikipedia <https://de.wikipedia.org/wiki/Pulsweitenmodulation>`_

Beim Einsatz von PWM mit dem Pico W gibt es einige Besonderheiten zu beachten. Betrachten wir hierzu folgendes Bild:

|pin_pwm|

Der Pico W bietet für jeden GPIO-Pin Unterstützung für PWM, allerdings sind nur 16 unabhängige PWM-Ausgänge (anstatt 30) verfügbar. Diese sind zwischen GP0 und GP15 auf der linken Seite verteilt, und die PWM-Ausgabe der rechten GPIO-Pins ist identisch mit der der linken.

Es ist ratsam, im Code nicht denselben PWM-Kanal für unterschiedliche Anwendungen zu nutzen. So sind beispielsweise GP0 und GP16 beide PWM_0A.

Nachdem wir nun das nötige Verständnis haben, wollen wir den Effekt der abklingenden LED erzielen.

* :ref:`cpn_led`

**Erforderliche Bauteile**

Für dieses Projekt benötigen wir die nachstehend aufgeführten Bauteile.

Ein komplettes Set ist definitiv praktisch; hier ist der entsprechende Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - Bestandteile des Sets
        - Link
    *   - Kepler Set
        - 450+
        - |link_kepler_kit|

Alternativ können die Komponenten auch einzeln erworben werden.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - Bauteil
        - Anzahl
        - Link

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
        - 1 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|


**Schaltplan**

|sch_led|

Dieses Projekt verwendet die gleiche Schaltung wie das erste Projekt :ref:`py_led`, jedoch unterscheidet sich die Art des Signals. Während das erste Projekt digitale Hoch- und Tiefpegel (0&1) direkt von GP15 ausgibt, um die LEDs ein- oder auszuschalten, wird in diesem Projekt ein PWM-Signal von GP15 zur Helligkeitssteuerung der LED verwendet.

**Verdrahtung**

|wiring_led|

**Code**

.. note::

    * Öffnen Sie die Datei ``2.3_fading_led.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny und klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, den Interpreter "MicroPython (Raspberry Pi Pico)" in der rechten unteren Ecke auszuwählen.

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import utime

    led = machine.PWM(machine.Pin(15))
    led.freq(1000)

    for brightness in range(0,65535,50):
        led.duty_u16(brightness)
        utime.sleep_ms(10)
    led.duty_u16(0)

Mit dem Ausführen des Codes wird die LED allmählich heller.

**Funktionsweise**

Hier ändern wir die Helligkeit der LED, indem wir den Tastgrad des PWM-Ausgangs von GP15 variieren. Werfen wir einen Blick auf diese Codezeilen.

.. code-block:: python
    :emphasize-lines: 4,5,8

    import machine
    import utime

    led = machine.PWM(machine.Pin(15))
    led.freq(1000)

    for brightness in range(0,65535,50):
        led.duty_u16(brightness)
        utime.sleep_ms(10)
    led.duty_u16(0)

* ``led = machine.PWM(machine.Pin(15))`` definiert den Pin GP15 als PWM-Ausgang.

* Mit der Zeile ``led.freq(1000)`` wird die PWM-Frequenz eingestellt, in diesem Fall auf 1000 Hz, was bedeutet, dass ein Zyklus 1 ms (1/1000) dauert.

* ``led.duty_u16()`` legt den Tastgrad fest, der als 16-Bit-Ganzzahl (2^16=65536) repräsentiert ist. Eine 0 steht für einen Tastgrad von 0%, d.h. der Pin bleibt während des gesamten Zyklus auf niedrigem Pegel. Der Wert 65535 entspricht einem Tastgrad von 100%, was bedeutet, dass der Ausgang durchgehend auf hohem Pegel ist und das Ergebnis '1' ist. Bei einem Wert von 32768 ist der Ausgang zur Hälfte der Zeit auf hohem Pegel, wodurch die LED nur halb so hell leuchtet.
