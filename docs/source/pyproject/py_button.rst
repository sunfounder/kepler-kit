.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_button:

2.5 Tastenwert auslesen
==============================================

Diese Pins haben sowohl Eingabe- als auch Ausgabefunktionen, wie es der Name GPIO (General-purpose input/output) bereits andeutet. Bisher haben wir die Ausgabefunktion genutzt; in diesem Kapitel verwenden wir die Eingabefunktion, um den Tastenwert einzulesen.

* :ref:`cpn_button`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Ein vollständiges Set zu kaufen ist natürlich bequem, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM SET
        - LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Alternativ können Sie die Komponenten auch einzeln über die folgenden Links erwerben.

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
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|

**Schaltplan**

|sch_button|

Solange eine Seite des Tastenpins mit 3,3 V verbunden ist und der andere Pin mit GP14 verbunden ist, wird GP14 hoch sein, wenn die Taste gedrückt wird. Wenn die Taste jedoch nicht gedrückt ist, befindet sich GP14 in einem unbestimmten Zustand und kann hoch oder niedrig sein. Um ein stabiles niedriges Signalniveau zu erhalten, wenn die Taste nicht gedrückt ist, muss GP14 über einen 10K-Pull-down-Widerstand erneut mit GND verbunden werden.

**Verdrahtung**

|wiring_button|

.. Folgen Sie der Richtung der Schaltung, um den Schaltkreis aufzubauen!

.. Hinweis::
    Ein Vierpol-Taster hat die Form eines H. Die beiden linken oder rechten Pins sind miteinander verbunden, sodass er die mittlere Lücke überspannt und somit zwei halbe Reihen mit der gleichen Reihennummer verbindet. (In meiner Schaltung sind beispielsweise E23 und F23 bereits verbunden, ebenso E25 und F25).

    Solange die Taste nicht gedrückt ist, sind die linken und rechten Pins voneinander unabhängig, und der Strom kann nicht von einer Seite zur anderen fließen.

**Code**

.. Hinweis::

    * Öffnen Sie die Datei ``2.5_read_button_value.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny, und klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, im unteren rechten Eck den "MicroPython (Raspberry Pi Pico)"-Interpreter auszuwählen.

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    button = machine.Pin(14, machine.Pin.IN)
    while True:
        if button.value() == 1:
            print("You pressed the button!")
            utime.sleep(1)

Sobald der Code ausgeführt wird, wird "Sie haben die Taste gedrückt!" in der Shell ausgegeben.

**Pull-Up-Arbeitsmodus**

Der nächste Abschnitt behandelt die Verdrahtung und den Code, wenn Sie den Taster im Pull-Up-Modus verwenden.

|sch_button_pullup|

|wiring_button_pullup|

Der einzige Unterschied, den Sie im Vergleich zum Pull-Down-Modus feststellen werden, ist, dass der 10K-Widerstand mit 3,3 V und die Taste mit GND verbunden ist. Dadurch erhält GP14 ein niedriges Signalniveau, wenn die Taste gedrückt wird, was das Gegenteil vom Pull-Down-Modus ist.
Ändern Sie also diesen Code einfach zu ``if button.value() == 0:``.

Weitere Referenzen finden Sie hier:

* `machine.Pin <https://docs.micropython.org/en/latest/library/machine.Pin.html>`_

