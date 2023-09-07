.. _py_joystick:

4.1 Den Joystick umschalten
================================

Wenn du viele Videospiele spielst, solltest du mit dem Joystick bestens vertraut sein.
Er wird normalerweise verwendet, um die Spielfigur zu bewegen, den Bildschirm zu drehen usw.

Das Grundprinzip hinter der Fähigkeit des Joysticks, dem Computer unsere Aktionen mitzuteilen, ist sehr einfach.
Man kann ihn sich als zwei senkrecht zueinander stehende Potentiometer vorstellen.
Diese beiden Potentiometer messen den analogen Wert des Joysticks in vertikaler und horizontaler Richtung, was in einem Wert (x,y) in einem ebenen rechtwinkligen Koordinatensystem resultiert.

Der Joystick dieses Sets hat auch einen digitalen Eingang, der aktiviert wird, wenn der Joystick gedrückt wird.

* :ref:`cpn_joystick`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir folgende Komponenten.

Es ist definitiv praktisch, ein ganzes Set zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM SET
        - LINK
    *   - Kepler Set
        - 450+
        - |link_kepler_kit|

Sie können die Teile auch einzeln über die untenstehenden Links kaufen.

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
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_joystick`
        - 1
        - 

**Schaltplan**

|sch_joystick|

Der SW-Pin ist mit einem 10K Pull-up-Widerstand verbunden, um ein stabiles High-Level am SW-Pin (Z-Achse) zu erhalten, wenn der Joystick nicht gedrückt ist; sonst wäre der SW in einem unbestimmten Zustand und der Ausgangswert könnte zwischen 0/1 variieren.

**Verdrahtung**

|wiring_joystick|


**Code**

.. note::

    * Öffnen Sie die Datei ``4.1_toggle_the_joystick.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny und klicken dann auf "Aktuelles Skript ausführen" oder drücken einfach F5.

    * Vergessen Sie nicht, den Interpreter "MicroPython (Raspberry Pi Pico)" in der unteren rechten Ecke auszuwählen.

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    x_joystick = machine.ADC(27)
    y_joystick = machine.ADC(26)
    z_switch = machine.Pin(22,machine.Pin.IN)

    while True:
        x_value = x_joystick.read_u16()
        y_value = y_joystick.read_u16()
        z_value = z_switch.value()
        print(x_value,y_value,z_value)
        utime.sleep_ms(200) 

Nachdem das Programm ausgeführt wurde, gibt die Shell die Werte x, y und z des Joysticks aus.

* Die Werte der x- und y-Achse sind analoge Werte, die zwischen 0 und 65535 variieren.
* Die Z-Achse ist ein digitaler Wert mit einem Status von 1 oder 0.
