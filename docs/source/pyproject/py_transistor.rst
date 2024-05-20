.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_transistor:

2.15 Zwei Arten von Transistoren
==========================================
Dieses Set ist mit zwei Arten von Transistoren ausgestattet, dem S8550 und dem S8050, wobei der erstere ein PNP- und der letztere ein NPN-Typ ist. Sie sehen sehr ähnlich aus, daher ist eine genaue Kontrolle der Beschriftungen erforderlich.
Wird ein High-Level-Signal durch einen NPN-Transistor geleitet, wird dieser aktiviert. Ein PNP-Transistor hingegen benötigt ein Low-Level-Signal zur Ansteuerung. Beide Transistortypen werden häufig in berührungslosen Schaltungen verwendet, wie auch in diesem Experiment.

|img_NPN&PNP|

Verwenden wir LED und Schalter, um den Umgang mit Transistoren zu verstehen!

:ref:`cpn_transistor`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist natürlich praktisch, gleich ein ganzes Set zu kaufen. Hier ist der Link dazu:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IM SET
        - LINK
    *   - Kepler-Set
        - 450+
        - |link_kepler_kit|

Die Komponenten können auch einzeln über die folgenden Links erworben werden.


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
        - 3(220Ω, 1KΩ, 10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|
    *   - 8
        - :ref:`cpn_transistor`
        - 1(S8050/S8550)
        - |link_transistor_buy|


**Anschluss des NPN (S8050) Transistors**

|sch_s8050|

In dieser Schaltung wird GP14 auf High gesetzt, wenn der Taster gedrückt wird.

Programmiert man GP15 auf einen hohen Ausgangspegel, so wird nach einem 1k-Strombegrenzungswiderstand (zum Schutz des Transistors) der S8050 (NPN-Transistor) zum Leiten gebracht und die LED leuchtet auf.

|wiring_s8050|

**Anschluss des PNP(S8550) Transistors**

|sch_s8550|

In dieser Schaltung ist GP14 standardmäßig auf Low und ändert auf High, wenn der Taster gedrückt wird.

Programmiert man GP15 auf einen niedrigen Ausgangspegel, so wird nach einem 1k-Strombegrenzungswiderstand (zum Schutz des Transistors) der S8550 (PNP-Transistor) zum Leiten gebracht und die LED leuchtet auf.

Der einzige Unterschied, den Sie zwischen dieser und der vorherigen Schaltung bemerken werden, besteht darin, dass in der vorherigen Schaltung die Kathode der LED mit dem **Kollektor** des **S8050 (NPN-Transistor)** und in dieser mit dem **Emitter** des **S8550 (PNP-Transistor)** verbunden ist.

|wiring_s8550|


**Code**

.. note::

    * Öffnen Sie die Datei ``2.15_transistor.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny, und klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, auf den "MicroPython (Raspberry Pi Pico)"-Interpreter in der unteren rechten Ecke zu klicken.

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    button = machine.Pin(14, machine.Pin.IN)
    signal = machine.Pin(15, machine.Pin.OUT)    

    while True:
        button_status = button.value()
        if button_status== 1:
            signal.value(1)
        elif button_status == 0:
            signal.value(0)


Beide Transistortypen können mit dem gleichen Code gesteuert werden. Drücken wir den Taster, sendet der Pico W ein High-Level-Signal an den Transistor; lassen wir los, wird ein Low-Level-Signal gesendet.
Wir sehen, dass sich in den beiden Schaltungen diametral entgegengesetzte Phänomene ergeben.

* Die Schaltung mit dem S8050 (NPN-Transistor) leuchtet auf, wenn der Taster gedrückt wird, das heißt, sie empfängt einen High-Level-Stromkreis;
* Die Schaltung mit dem S8550 (PNP-Transistor) leuchtet auf, wenn sie losgelassen wird, das heißt, sie empfängt einen Low-Level-Stromkreis.
