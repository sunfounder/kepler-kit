.. _py_slide:

2.7 Nach Links und Rechts Schalten
====================================

|img_slide|

Der Schiebeschalter ist ein Gerät mit drei Anschlüssen, wobei der mittlere Anschluss (Pin 2) der gemeinsame Anschluss ist. Wird der Schalter nach links geschaltet, sind die beiden linken Pins miteinander verbunden. Wird er nach rechts geschaltet, sind die beiden rechten Pins verbunden.

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Ein komplettes Kit zu kaufen, ist definitiv praktisch, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Kepler-Kit
        - 450+
        - |link_kepler_kit|


Sie können die Bauteile auch einzeln über die folgenden Links erwerben.


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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_capacitor`
        - 1(104)
        - |link_capacitor_buy|
    *   - 7
        - :ref:`cpn_slide_switch`
        - 1
        - 

**Schaltplan**

|sch_slide|

Bei einer Schaltung nach rechts oder links wird GP14 einen unterschiedlichen Pegel erreichen.

Der 10K-Widerstand dient dazu, GP14 während des Umschaltens auf einem niedrigen Pegel zu halten (nicht ganz nach links und nicht ganz nach rechts geschaltet).

Der 104-Keramikkondensator wird hier eingesetzt, um Rauschen zu eliminieren.

* :ref:`cpn_slide_switch`
* :ref:`cpn_capacitor`

**Verdrahtung**

|wiring_slide|

**Code**

.. note::

    * Öffnen Sie die Datei ``2.7_slide_switch.py`` im Ordner ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny, und klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, den "MicroPython (Raspberry Pi Pico)"-Interpreter in der unteren rechten Ecke auszuwählen.

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    button = machine.Pin(14, machine.Pin.IN)
    while True:
        if button.value() == 0:
            print("The switch works!")
            utime.sleep(1)

Nach dem Ausführen des Programms erscheint im Shell die Meldung "The switch works!", wenn der Schiebeschalter nach rechts geschaltet wird.
