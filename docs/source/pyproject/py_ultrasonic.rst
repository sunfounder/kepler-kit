.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_ultrasonic:

6.1 Abstandsmessung
======================================

Das Ultraschallsensormodul funktioniert nach dem Prinzip von Sonar- und Radarsystemen, um die Entfernung zu einem Objekt zu ermitteln.

* :ref:`cpn_ultrasonic`

**Benötigte Komponenten**

Für dieses Projekt werden die folgenden Komponenten benötigt.

Ein Komplettset zu kaufen ist definitiv praktisch, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM SET
        - LINK
    *   - Kepler-Set	
        - 450+
        - |link_kepler_kit|

Sie können die Teile auch einzeln über die untenstehenden Links erwerben.


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
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**Schaltplan**

|sch_ultrasonic|

**Verdrahtung**

|wiring_ultrasonic|

**Code**

.. note::

    * Öffnen Sie die Datei ``6.1_measuring_distance.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny. Klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, den "MicroPython (Raspberry Pi Pico)"-Interpreter in der rechten unteren Ecke auszuwählen. 

    * Für detaillierte Anleitungen verweisen wir auf :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

    TRIG = machine.Pin(17,machine.Pin.OUT)
    ECHO = machine.Pin(16,machine.Pin.IN)

    def distance():
        TRIG.low()
        time.sleep_us(2)
        TRIG.high()
        time.sleep_us(10)
        TRIG.low()
        while not ECHO.value():
            pass
        time1 = time.ticks_us()
        while ECHO.value():
            pass
        time2 = time.ticks_us()
        during = time.ticks_diff(time2,time1)
        return during * 340 / 2 / 10000

    while True:
        dis = distance()
        print ('Distance: %.2f' % dis)
        time.sleep_ms(300)

Sobald das Programm läuft, wird die Shell den Abstand des Ultraschallsensors zum Hindernis vor ihm ausgeben.

**Funktionsweise**

Ultraschallsensoren erzeugen hochfrequente Schallwellen (Ultraschallwellen), die von der Sendesonde ausgesendet werden. Trifft diese Ultraschallwelle auf ein Objekt, wird sie als Echo reflektiert und von der Empfangssonde detektiert. Durch die Berechnung der Zeit von der Aussendung bis zum Empfang lässt sich die Entfernung ermitteln. Auf diesem Prinzip basiert die Funktion ``distance()``.

.. code-block:: python

    def distance():
        TRIG.low()
        time.sleep_us(2)
        TRIG.high()
        time.sleep_us(10)
        TRIG.low()
        while not ECHO.value():
            pass
        time1 = time.ticks_us()
        while ECHO.value():
            pass
        time2 = time.ticks_us()
        during = time.ticks_diff(time2,time1)
        return during * 340 / 2 / 10000

* Dabei dienen die ersten paar Zeilen dazu, eine 10µs Ultraschallwelle auszusenden.

.. code-block:: python

    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()

* Anschließend wird das Programm angehalten und die aktuelle Zeit erfasst, sobald die Ultraschallwelle ausgesendet wurde.

.. code-block:: python

        while not ECHO.value():
            pass
        time1 = time.ticks_us()

* Daraufhin wird das Programm erneut pausiert. Nachdem das Echo empfangen wurde, wird die aktuelle Zeit erneut erfasst.

.. code-block:: python

        while ECHO.value():
            pass
        time2 = time.ticks_us()

* Abschließend wird anhand der Zeitdifferenz zwischen den beiden Erfassungen die Schallgeschwindigkeit (340 m/s) mit der Zeit multipliziert, um die doppelte Entfernung zwischen dem Ultraschallmodul und dem Hindernis zu erhalten (also einen Rundflug der Ultraschallwellen vom Modul zum Hindernis). Die Umrechnung in Zentimeter liefert den benötigten Rückgabewert.

.. code-block:: python

        during = time.ticks_diff(time2,time1)
        return during * 340 / 2 / 10000

Beachten Sie, dass der Ultraschallsensor das Programm anhält, wenn er arbeitet, was zu Verzögerungen bei der Entwicklung komplexer Projekte führen kann.

