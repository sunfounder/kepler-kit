.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_ac_buz:

3.1 Piepton
==================

Der aktive Summer ist ein typisches digitales Ausgabegerät, dessen Anwendung genauso einfach ist wie das Einschalten einer LED!

* :ref:`cpn_buzzer`

**Erforderliche Komponenten**

Für dieses Projekt benötigen wir folgende Bauteile.

Ein Gesamtpaket zu kaufen ist natürlich bequemer, hier ist der Link dazu:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM SET
        - LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Sie können die Bauteile aber auch einzeln unter den folgenden Links erwerben.

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
        - :ref:`cpn_transistor`
        - 1 (S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1 (1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Aktiver :ref:`cpn_buzzer`
        - 1
        - 

**Schaltbild**

|sch_buzzer|

Wird der GP15-Ausgang auf "High" gesetzt, wird der S8050 (NPN-Transistor) nach dem 1K-Strombegrenzungswiderstand (zum Schutz des Transistors) leitend und der Summer gibt einen Ton ab.

Die Aufgabe des S8050 (NPN-Transistor) besteht darin, den Strom zu verstärken, damit der Summer lauter tönt. Tatsächlich können Sie den Summer auch direkt an GP15 anschließen, werden dann aber feststellen, dass der Ton leiser ist.

**Verdrahtung**

Im Kit sind zwei verschiedene Summertypen enthalten. 
Wir verwenden den aktiven Summer. Drehen Sie beide um, der versiegelte Rücken (nicht die freiliegende Leiterplatte) ist der, den wir benötigen.

|img_buzzer|

Für den Betrieb des Summers ist ein Transistor erforderlich, hier verwenden wir den S8050 (NPN-Transistor).

|wiring_beep|

**Code**

.. note::

    * Öffnen Sie die Datei ``3.1_beep.py`` im Ordner ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny. Klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, den "MicroPython (Raspberry Pi Pico)"-Interpreter in der rechten unteren Ecke auszuwählen.

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    buzzer = machine.Pin(15, machine.Pin.OUT)
    while True:
        for i in range(4):
            buzzer.value(1)
            utime.sleep(0.3)
            buzzer.value(0)
            utime.sleep(0.3)
        utime.sleep(1)

Nach dem Ausführen des Codes hören Sie jede Sekunde einen Piepton.
