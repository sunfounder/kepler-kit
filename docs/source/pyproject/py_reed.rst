.. _py_reed:

2.9 Fühle den Magnetismus
================================

Der gebräuchlichste Typ eines Reed-Schalters besteht aus einem Paar magnetisierbarer, flexibler Metallzungen, deren Enden bei geöffnetem Schalter durch eine kleine Lücke getrennt sind.

Ein Magnetfeld, erzeugt entweder durch einen Elektromagneten oder einen Permanentmagneten, führt dazu, dass sich die Zungen anziehen und somit einen elektrischen Stromkreis schließen. 
Die Federkraft der Zungen bewirkt, dass sie sich trennen und den Stromkreis unterbrechen, sobald das Magnetfeld erlischt.

Ein typisches Anwendungsbeispiel für einen Reed-Schalter ist die Überwachung des Öffnens von Türen oder Fenstern in einer Alarmanlage.

* :ref:`cpn_reed`

**Benötigte Komponenten**

Für dieses Projekt werden die folgenden Komponenten benötigt.

Ein Komplettset zu kaufen, ist definitiv praktisch. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM SET
        - LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Die Teile können auch einzeln über die folgenden Links erworben werden.

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
        - :ref:`cpn_reed`
        - 1
        - 

**Schaltplan**

|sch_reed|

Standardmäßig ist GP14 niedrig; der Wert wird hoch, sobald ein Magnet in der Nähe des Reed-Schalters ist.

Der 10K-Widerstand dient dazu, GP14 auf einem konstant niedrigen Level zu halten, wenn kein Magnet in der Nähe ist.

**Verdrahtung**

|wiring_reed|

**Code**

.. note::

    * Öffnen Sie die Datei ``2.9_feel_the_magnetism.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny und klicken Sie auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, den "MicroPython (Raspberry Pi Pico)"-Interpreter in der rechten unteren Ecke auszuwählen.

    * Für ausführliche Anleitungen beachten Sie bitte :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    reed = machine.Pin(14, machine.Pin.IN)
    while True:
        if reed.value() == 1:
            print("There are magnets here!!")
            utime.sleep(1)

Läuft der Code, wird GP14 hoch, wenn ein Magnet in der Nähe des Reed-Schalters ist, ansonsten niedrig. Ganz wie der Knopf im Kapitel :ref:`py_button`.

**Mehr erfahren**

Dieses Mal haben wir eine flexible Art der Schalterbenutzung erprobt: Unterbrechungsanfragen, auch IRQs genannt.

Stellen Sie sich zum Beispiel vor, Sie lesen Seite für Seite ein Buch, als wäre ein Programm einen Thread am Ausführen. Plötzlich kommt jemand und stellt Ihnen eine Frage, unterbricht also Ihre Lektüre. Diese Person führt die Unterbrechungsanfrage aus: Sie sollen kurz stoppen, die Frage beantworten und dann Ihre Lektüre fortsetzen.

Die Unterbrechungsanfragen in MicroPython funktionieren ähnlich, sie erlauben bestimmten Aktionen, das Hauptprogramm zu unterbrechen.

.. note::

    * Öffnen Sie die Datei ``2.9_feel_the_magnetism_irq.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny und klicken Sie auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, den "MicroPython (Raspberry Pi Pico)"-Interpreter in der rechten unteren Ecke auszuwählen.

    * Für ausführliche Anleitungen beachten Sie bitte :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    reed_switch = machine.Pin(14, machine.Pin.IN)

    def detected(pin):
        print("Magnet!")

    reed_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=detected)

Zunächst wird eine Callback-Funktion ``detected(pin)`` definiert, die als Unterbrechungsbehandler dient. Sie wird ausgeführt, wenn eine Unterbrechungsanfrage ausgelöst wird. Dann wird im Hauptprogramm eine Unterbrechungsanfrage eingerichtet, die aus zwei Teilen besteht: dem ``trigger`` und dem ``handler``.

Im Programm ist ``trigger`` ``IRQ_RISING``, was bedeutet, dass der Wert des Pins von niedrig auf hoch wechselt (also beim Tastendruck).

``handler`` ist ``detected``, die vorher definierte Callback-Funktion.

* `machine.Pin.irq - Micropython Docs <https://docs.micropython.org/en/latest/library/machine.Pin.html#machine.Pin.irq>`

