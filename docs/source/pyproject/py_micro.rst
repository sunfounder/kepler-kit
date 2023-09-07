.. _py_micro:

2.8 Sanft Drücken
==========================

|img_micro_switch|

Ein Mikroschalter ist ebenfalls ein Gerät mit 3 Anschlüssen. Die Reihenfolge der Anschlüsse ist C (gemeinsamer Pin), NO (normalerweise offen) und NC (normalerweise geschlossen).

Wenn der Mikroschalter nicht gedrückt ist, sind 1 (C) und 3 (NC) miteinander verbunden. Wird er gedrückt, sind 1 (C) und 2 (NO) miteinander verbunden.

* :ref:`cpn_micro_switch`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Ein Komplettset zu kaufen ist definitiv praktisch, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IM SET
        - LINK
    *   - Kepler-Set	
        - 450+
        - |link_kepler_kit|


Sie können die einzelnen Teile auch über die untenstehenden Links kaufen.


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
        - :ref:`cpn_micro_switch`
        - 1
        - 


**Schaltplan**

|sch_limit_sw|

Standardmäßig ist GP14 niedrig und wird hoch, wenn der Schalter gedrückt wird.

Der 10K-Widerstand dient dazu, GP14 während des Drückens niedrig zu halten.

Der 104 Keramikkondensator wird hier verwendet, um Rauschen zu eliminieren.



**Verdrahtung**

|wiring_limit_sw|


**Code**

.. note::

    * Öffnen Sie die Datei ``2.8_micro_switch.py`` im Pfad ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny und klicken Sie auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, im unteren rechten Bereich auf den "MicroPython (Raspberry Pi Pico)"-Interpreter zu klicken. 

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    button = machine.Pin(14, machine.Pin.IN)
    while True:
        if button.value() == 1:
            print("The switch works!")
            utime.sleep(1)


Nachdem das Programm gelaufen ist, erscheint "Der Schalter funktioniert!" im Shell-Fenster, wenn Sie den Schiebeschalter nach rechts bewegen.
