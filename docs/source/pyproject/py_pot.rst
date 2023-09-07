.. _py_pot:

2.11 Den Drehregler betätigen
=============================

In den vorherigen Projekten haben wir den digitalen Eingang des Pico W genutzt.
Beispielsweise kann ein Knopf den Pin von einem niedrigen (aus) zu einem hohen Pegel (ein) ändern. Das ist ein binärer Arbeitszustand.

Der Pico W ist jedoch auch in der Lage, eine andere Art von Eingangssignal zu empfangen: den analogen Eingang.
Dieser kann sich in einem Zustand von vollständig geschlossen bis vollständig geöffnet befinden und bietet ein Spektrum an möglichen Werten.
Der analoge Eingang erlaubt es dem Mikrocontroller, die Lichtintensität, Schallintensität, Temperatur, Feuchtigkeit usw. der physischen Welt zu erfassen.

Normalerweise benötigt ein Mikrocontroller zusätzliche Hardware für den analogen Eingang - den Analog-Digital-Umsetzer (ADC).
Der Pico W verfügt jedoch bereits über einen integrierten ADC, den wir direkt nutzen können.


|pin_adc|

Der Pico W besitzt drei GPIO-Pins, die für analogen Eingang genutzt werden können: GP26, GP27, GP28, also analoge Kanäle 0, 1 und 2.
Zudem gibt es einen vierten analogen Kanal, der mit dem eingebauten Temperatursensor verbunden ist und hier nicht weiter erläutert wird.

In diesem Projekt versuchen wir, den analogen Wert eines Potentiometers auszulesen.

* :ref:`cpn_potentiometer`

**Erforderliche Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist sicherlich praktisch, ein komplettes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - KOMPONENTEN IN DIESEM KIT
        - LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Sie können die Komponenten auch einzeln über die unten stehenden Links kaufen.


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
        - 1 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_potentiometer`
        - 1
        - |link_potentiometer_buy|


**Schaltplan**

|sch_pot|

Das Potentiometer ist ein analoges Bauteil, das in zwei verschiedene Richtungen gedreht werden kann.

Schließen Sie den mittleren Pin des Potentiometers an den analogen Pin GP28 an. Der Raspberry Pi Pico W verfügt über einen mehrkanaligen, 16-bit Analog-Digital-Umsetzer. Das bedeutet, dass die Eingangsspannung zwischen 0 und der Betriebsspannung (3,3V) auf einen Ganzzahlwert zwischen 0 und 65535 abgebildet wird. Der Wertebereich von GP28 reicht also von 0 bis 65535.

Die Berechnungsformel lautet wie folgt:

    (Vp/3.3V) x 65535 = Ap

Programmieren Sie dann den Wert von GP28 (Potentiometer) als PWM-Wert von GP15 (LED).
Sie werden feststellen, dass die Helligkeit der LED sich gleichzeitig ändert, wenn Sie das Potentiometer drehen.

**Verdrahtung**

|wiring_pot|

**Code**

.. note::

    * Öffnen Sie die Datei ``2.11_turn_the_knob.py`` im Pfad ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny, klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, den Interpreter "MicroPython (Raspberry Pi Pico)" in der rechten unteren Ecke auszuwählen.

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    potentiometer = machine.ADC(28)
    led = machine.PWM(machine.Pin(15))
    led.freq(1000)

    while True:
        value = potentiometer.read_u16()
        print(value)
        led.duty_u16(value)
        utime.sleep_ms(200)

Wenn das Programm läuft, können wir den derzeit von Pin GP28 gelesenen analogen Wert im Shell-Fenster sehen.
Drehen Sie den Drehregler, und der Wert wird sich von 0 auf 65535 ändern.
Gleichzeitig wird die Helligkeit der LED mit dem Anstieg des analogen Werts zunehmen.

**Funktionsweise**

.. code-block:: python

    potentiometer = machine.ADC(28)

Zugriff auf den ADC, der mit einer durch die ID identifizierten Quelle verbunden ist. In diesem Beispiel handelt es sich um GP28.

.. code-block:: python

    potentiometer.read_u16()

Führt eine analoge Messung durch und gibt einen Ganzzahlwert im Bereich von 0 bis 65535 zurück. Der Rückgabewert stellt die rohe Messung dar, die vom ADC erfasst und so skaliert wurde, dass der Mindestwert 0 und der Höchstwert 65535 beträgt.


* `machine.ADC - MicroPython Dokumentation <https://docs.micropython.org/en/latest/library/machine.ADC.html>`_

