.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_led:

2.1 Hallo, LED!
=======================================

Genau wie das Ausgeben von "Hallo, Welt!" der erste Schritt beim Erlernen der Programmierung ist, stellt die Ansteuerung einer LED mit einem Programm die traditionelle Einführung in die physische Programmierung dar.

* :ref:`cpn_led`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir folgende Komponenten:

Es ist definitiv praktisch, ein komplettes Set zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM SET
        - LINK
    *   - Kepler-Set
        - 450+
        - |link_kepler_kit|

Die Einzelteile können auch über die unten stehenden Links separat erworben werden.

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

**Schaltplan**

|sch_led|

Dieser Schaltkreis funktioniert nach einem einfachen Prinzip, die Stromrichtung ist in der Abbildung dargestellt. Die LED leuchtet auf, wenn GP15 eine hohe Ausgangsspannung (3,3 V) liefert, und erlischt, wenn GP15 eine niedrige Ausgangsspannung (0 V) liefert.

**Verdrahtung**

|wiring_led|

Um den Schaltkreis aufzubauen, folgen wir der Stromrichtung!

1. Die LED wird über den GP15-Pin der Pico-W-Platine mit Strom versorgt; hier beginnt der Schaltkreis.
#. Um die LED zu schützen, muss der Strom durch einen 220-Ohm-Widerstand fließen. Ein Ende des Widerstands sollte in die gleiche Reihe wie der Pico-W GP15-Pin (Reihe 20 in meinem Schaltkreis) eingefügt werden, das andere Ende in eine freie Reihe des Steckbretts (Reihe 24).

   .. note::
       Der Farbring des 220-Ohm-Widerstands ist rot, rot, schwarz, schwarz und braun.

#. Wenn Sie die LED aufnehmen, stellen Sie fest, dass einer der Anschlüsse länger ist als der andere. Verbinden Sie den längeren Anschluss mit der gleichen Reihe wie der Widerstand und den kürzeren Anschluss mit der Reihe gegenüber der Mittellücke auf dem Steckbrett.

   .. note::
       Der längere Anschluss ist die Anode und repräsentiert die positive Seite des Schaltkreises; der kürzere ist die Kathode und steht für die negative Seite.

       Die Anode muss über einen Widerstand mit dem GPIO-Pin verbunden sein; die Kathode muss mit dem GND-Pin verbunden sein.

#. Verwenden Sie ein Stecker-zu-Stecker (M2M) Verbindungskabel, um den kurzen Anschluss der LED mit der negativen Stromschiene des Steckbretts zu verbinden.
#. Verbinden Sie den GND-Pin des Pico W mit der negativen Stromschiene des Steckbretts mithilfe eines Verbindungskabels.

**Code**

.. note::

   * Öffnen Sie die Datei ``2.1_hello_led.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny. Klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5, um es auszuführen.

   * Vergessen Sie nicht, den "MicroPython (Raspberry Pi Pico)"-Interpreter in der rechten unteren Ecke auszuwählen.

   * Für detaillierte Anleitungen beziehen Sie sich bitte auf :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    
    led = machine.Pin(15, machine.Pin.OUT)
    while True:
        led.value(1)
        utime.sleep(2)
        led.value(0)
        utime.sleep(2)

Nachdem der Code ausgeführt wurde, sehen Sie die LED blinken.

**Wie funktioniert es?**

Die Bibliothek „machine“ wird benötigt, um GPIO zu nutzen.

.. code-block:: python

    import machine

Diese Bibliothek enthält alle Anweisungen, die zur Kommunikation zwischen MicroPython und Pico W erforderlich sind. Fehlt diese Zeile im Code, können wir keine GPIOs steuern.

Das Nächste, was auffällt, ist diese Zeile:

.. code-block:: python

    led = machine.Pin(15, machine.Pin.OUT)

Hier wird das Objekt ``led`` definiert. Technisch gesehen könnte es jeden beliebigen Namen haben, wie x, y, Banane oder Michael_Jackson. Um die Lesbarkeit des Programms zu gewährleisten, sollte ein beschreibender Name gewählt werden.

Im zweiten Teil dieser Zeile (dem Teil nach dem Gleichheitszeichen) rufen wir die Funktion „Pin“ aus der „machine“-Bibliothek auf. Diese dient dazu, den GPIO-Pins des Pico W zu sagen, was sie tun sollen. Die Funktion „Pin“ hat zwei Parameter: Der erste (15) gibt an, welcher Pin eingestellt werden soll; der zweite Parameter (machine.Pin.OUT) gibt an, dass der Pin als Ausgang und nicht als Eingang fungieren soll.

Der oben stehende Code hat den Pin "eingestellt", aber er wird die LED noch nicht zum Leuchten bringen. Dazu müssen wir den Pin auch "nutzen".

.. code-block:: python

    led.value(1)

Der GP15-Pin wurde zuvor eingerichtet und heißt ``led``. Die Funktion dieser Anweisung besteht darin, den Wert von ``led`` auf 1 zu setzen.

Um GPIO zu verwenden, sind folgende Schritte notwendig:

* **`machine`-Bibliothek importieren**: Dies ist ein notwendiger Schritt und wird nur einmal durchgeführt.
* **GPIO einstellen**: Vor der Nutzung muss jeder Pin konfiguriert werden.
* **Verwenden**: Durch Zuweisung eines Wertes wird der Arbeitszustand des Pins verändert.

Folgt man diesen Anweisungen, erhält man beispielsweise folgenden Code:

.. code-block:: python

    import machine
    led = machine.Pin(15, machine.Pin.OUT)
    led.value(1)

Führt man diesen aus, wird die LED leuchten.

Als nächstes fügen wir die "Ausschalt"-Anweisung hinzu:

.. code-block:: python

    import machine
    led = machine.Pin(15, machine.Pin.OUT)
    led.value(1)
    led.value(0)

Gemäß dem Code sollte das Programm die LED zunächst einschalten und dann wieder ausschalten. 
In der Praxis stellt sich jedoch heraus, dass dies nicht der Fall ist.
Die LED leuchtet nicht, da die beiden Zeilen sehr schnell nacheinander ausgeführt werden, schneller als das menschliche Auge reagieren kann.
Das lässt sich beheben, indem das Programm verlangsamt wird.

Für diesen Zweck sollte die zweite Zeile des Programms wie folgt aussehen:

.. code-block:: python

    import utime

Ähnlich wie bei ``machine`` importieren wir hier die Bibliothek ``utime``, die Zeitfunktionen verwaltet. 
Nun fügen wir zwischen ``led.value(1)`` und ``led.value(0)`` eine Verzögerung von 2 Sekunden ein.

.. code-block:: python

    utime.sleep(2)

So sollte der Code jetzt aussehen.
Beim Ausführen wird nun zuerst die LED eingeschaltet und dann ausgeschaltet:

.. code-block:: python

    import machine
    import utime
    led = machine.Pin(15, machine.Pin.OUT)
    led.value(1)
    utime.sleep(2)
    led.value(0)

Zuletzt soll die LED blinken. 
Dafür erstellen wir eine Schleife und ändern das Programm entsprechend.

.. code-block:: python

    import machine
    import utime
    
    led = machine.Pin(15, machine.Pin.OUT)
    while True:
        led.value(1)
        utime.sleep(2)
        led.value(0)
        utime.sleep(2)

* :ref:`While-Schleifen`

**Weitere Informationen**

Normalerweise gibt es eine API-Dokumentation, die mit der Bibliothek verknüpft ist. 
Diese enthält alle notwendigen Informationen für die Verwendung der Bibliothek, einschließlich detaillierter Beschreibungen von Funktionen, Klassen, Rückgabetypen, Parameterarten usw.

In diesem Artikel haben wir MicroPythons ``machine`` und ``utime`` Bibliotheken verwendet; weitere Verwendungsmöglichkeiten finden Sie hier:

* `machine.Pin <https://docs.micropython.org/en/latest/library/machine.Pin.html>`_

* `utime <https://docs.micropython.org/en/latest/library/utime.html>`_

Um dieses Beispiel des LED-Blinkens zu verstehen, lesen Sie bitte die API-Dokumentation!

.. note::

    * Öffnen Sie die Datei ``2.1_hello_led_2.py`` im Ordner ``kepler-kit-main/micropython`` oder kopieren Sie den Code in Thonny. Dann klicken Sie auf "Aktuelles Skript ausführen" oder drücken einfach F5.
  
    * Vergessen Sie nicht, den "MicroPython (Raspberry Pi Pico)"-Interpreter in der rechten unteren Ecke auszuwählen.
  
    * Für detaillierte Anleitungen beachten Sie bitte :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    led = machine.Pin(15, machine.Pin.OUT)
    while True:
        led.toggle()
        utime.sleep(1)
