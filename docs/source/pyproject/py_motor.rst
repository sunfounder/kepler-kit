.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_motor:

3.5 Kleiner Ventilator
=======================


Nun verwenden wir den TA6586, um den Gleichstrommotor im Uhrzeigersinn und gegen den Uhrzeigersinn anzutreiben.
Da der Gleichstrommotor einen vergleichsweise hohen Strom benötigt, setzen wir hier aus Sicherheitsgründen ein Netzteilmodul zur Stromversorgung des Motors ein.

* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

**Benötigte Bauteile**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist durchaus praktisch, ein komplettes Set zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung
        - TEILE IN DIESEM KIT
        - LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Sie können die Bauteile auch einzeln über die unten stehenden Links erwerben.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - BAUTEIL
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
        - :ref:`cpn_ta6586`
        - 1
        - 
    *   - 6
        - :ref:`cpn_motor`
        - 1
        - |link_motor_buy| 
    *   - 7
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 8
        - 18650 Batterie
        - 1
        -  
    *   - 9
        - Batteriehalter
        - 1
        -  


**Schaltplan**

|sch_motor|


**Verdrahtung**

.. note::

    * Da Gleichstrommotoren einen hohen Strom benötigen, verwenden wir hier aus Sicherheitsgründen ein Li-Po-Ladegerätmodul zur Stromversorgung des Motors.
    * Stellen Sie sicher, dass Ihr Li-Po-Ladegerätmodul wie im Schaltplan gezeigt angeschlossen ist. Andernfalls besteht die Gefahr eines Kurzschlusses, der Ihre Batterie und Schaltung beschädigen könnte.


|wiring_motor|


**Code**

.. note::

    * Öffnen Sie die Datei ``3.5_small_fan.py`` im Pfad ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny, und klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, den "MicroPython (Raspberry Pi Pico)"-Interpreter in der unteren rechten Ecke auszuwählen.

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    motor1A = machine.Pin(14, machine.Pin.OUT)
    motor2A = machine.Pin(15, machine.Pin.OUT)

    def clockwise():
        motor1A.high()
        motor2A.low()

    def anticlockwise():
        motor1A.low()
        motor2A.high()

    def stopMotor():
        motor1A.low()
        motor2A.low()

    while True:
        clockwise()
        utime.sleep(1)
        stopMotor()
        utime.sleep(1)
        anticlockwise()
        utime.sleep(1)
        stopMotor()
        utime.sleep(1)

Sobald das Programm läuft, wird der Motor in einem regelmäßigen Muster hin und her drehen.


.. note::

    * Wenn der Motor sich nach dem Klicken auf die Stop-Taste weiterdreht, müssen Sie zu diesem Zeitpunkt den **RUN**-Pin am Pico W mit einem Draht auf GND zurücksetzen und dann diesen Draht entfernen, um den Code erneut auszuführen.
    * Dies liegt daran, dass der Motor mit zu hohem Strom arbeitet, was dazu führen kann, dass der Pico W die Verbindung zum Computer verliert.

    |wiring_run_reset|
