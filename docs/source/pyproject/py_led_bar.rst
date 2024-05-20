.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_led_bar:

2.2 Anzeige des Pegels
=============================

Das erste Projekt besteht einfach darin, eine LED blinken zu lassen. Für dieses Projekt verwenden wir die LED-Balkenanzeige, die aus 10 LEDs in einem Kunststoffgehäuse besteht und normalerweise zur Anzeige von Leistung oder Lautstärke verwendet wird.

|img_led_bar_pin|

* :ref:`cpn_led_bar`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Bauteile.

Es ist definitiv praktisch, ein ganzes Set zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM SET
        - LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Sie können die Teile auch einzeln über die untenstehenden Links kaufen.

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
        - 10 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led_bar`
        - 1
        - 

**Schaltplan**

|sch_ledbar|

In der LED-Balkenanzeige gibt es 10 LEDs, von denen jede individuell gesteuert werden kann. Die Anode jeder LED ist mit GP6*GP15 verbunden, die Kathode über einen 220-Ohm-Widerstand mit GND.

**Verdrahtung**

|wiring_ledbar|

**Code**

.. note::

    * Öffnen Sie die Datei ``2.2_display_the_level.py`` im Ordner ``kepler-kit-main/micropython`` oder kopieren Sie den Code in Thonny und klicken Sie dann auf "Run Current Script" oder drücken einfach F5.

    * Vergessen Sie nicht, den "MicroPython (Raspberry Pi Pico)"-Interpreter in der rechten unteren Ecke auszuwählen.
  
    * Für detaillierte Anleitungen beachten Sie bitte :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    pin = [6,7,8,9,10,11,12,13,14,15]
    led= []
    for i in range(10):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

    while True:
        for i in range(10):
            led[i].toggle()
            utime.sleep(0.2)

Auf der LED-Balkenanzeige sehen Sie, dass die LEDs in einer Sequenz aufleuchten und wieder erlöschen, während das Programm läuft.


**Wie funktioniert das?**

Die LED-Balkenanzeige besteht aus zehn LEDs, die von zehn Pins gesteuert werden. Das bedeutet, dass wir diese Pins definieren müssen.
Es wäre zu mühsam, sie einzeln zu definieren. Daher verwenden wir hier ``Lists``.

.. note::
    Python-Listen sind einer der vielseitigsten Datentypen, die es uns ermöglichen, mit mehreren Elementen gleichzeitig zu arbeiten. Sie werden durch das Platzieren von Elementen in eckigen Klammern [] erstellt, die durch Kommas getrennt sind.

.. code-block:: python

    pin = [6,7,8,9,10,11,12,13,14,15]    

Mit dieser Codezeile wird eine Liste ``pin`` definiert, die die zehn Elemente ``6,7,8,9,10,11,12,13,14,15`` enthält.
Wir können den Index-Operator [] verwenden, um auf ein Element in einer Liste zuzugreifen. In Python beginnen die Indizes bei 0. Daher wird eine Liste mit 10 Elementen einen Index von 0 bis 9 haben.
Bei dieser Liste als Beispiel ist ``pin[0]`` gleich ``6`` und ``pin[4]`` gleich ``10``.

Als Nächstes deklarieren Sie eine leere Liste ``led``, die zur Definition von zehn LED-Objekten verwendet wird.

.. code-block:: python

    led = []    

Aufgrund der Länge der Liste, die 0 beträgt, funktionieren direkte Operationen auf dem Array, wie zum Beispiel das Drucken von ``led[0]``, nicht. Es gibt neue Elemente, die wir hinzufügen müssen.

.. code-block:: python

    led.append(None)

Durch diese ``append()`` Methode hat die Liste ``led`` ihr erstes Element erhalten, mit einer Länge von 1, und ``led[0]`` wird zu einem gültigen Element, obwohl sein aktueller Wert ``None`` ist (was für Null steht).

Der nächste Schritt besteht darin, ``led[0]``, die an Pin 6 angeschlossene LED, als das erste LED-Objekt zu definieren.

.. code-block:: python

    led[0] = machine.Pin(6, machine.Pin.OUT)

Das erste LED-Objekt ist nun definiert.

Wie Sie sehen können, haben wir die zehn Pin-Nummern als Liste **pin** erstellt, die wir in diese Zeile einfügen können, um Massenoperationen zu erleichtern.

.. code-block:: python

    led[0] = machine.Pin(pin[0], machine.Pin.OUT)

Verwenden Sie eine ``for``-Schleife, damit alle 10 Pins den obigen Befehl ausführen.

.. code-block:: python

    import machine

    pin = [6,7,8,9,10,11,12,13,14,15]
    led = []
    for i in range(10):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

* :ref:`syntax_list`
* :ref:`For-Schleifen`

Verwenden Sie eine weitere ``for``-Schleife, um die zehn LEDs auf der LED-Balkenanzeige nacheinander umzuschalten.

.. code-block:: python

    for i in range(10):
        led[i].toggle()
        utime.sleep(0.2)

Der Code wird abgeschlossen, indem der obige Codeblock in eine While-Schleife eingefügt wird.

.. code-block:: python

    import machine
    import utime

    pin = [6,7,8,9,10,11,12,13,14,15]
    led = []
    for i in range(10):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

    while True:
        for i in range(10):
            led[i].toggle()
            utime.sleep(0.2)

