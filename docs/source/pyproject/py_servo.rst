.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_servo:

3.7 Schwingender Servo
=======================

In diesem Bausatz befinden sich neben LEDs und passivem Summer auch ein durch PWM-Signale gesteuertes Gerät, nämlich der Servo.

Der Servo ist ein Positions- (Winkel-) Servo, ideal geeignet für Steuerungssysteme, die konstante Winkeländerungen erfordern und aufrechterhalten können. Er findet häufig Anwendung in hochwertigen ferngesteuerten Spielzeugen, wie etwa Flugzeug-, U-Boot-Modellen und ferngesteuerten Robotern.

Versuchen wir nun, den Servo zum Schwingen zu bringen!

* :ref:`cpn_servo`

**Benötigte Bauteile**

Für dieses Projekt benötigen wir folgende Komponenten.

Es ist definitiv praktisch, das gesamte Set zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung	
        - BAUTEILE IM SET
        - LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

Die Bauteile können auch einzeln über die nachstehenden Links erworben werden.

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
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|

**Schaltplan**

|sch_servo|

**Verdrahtung**

|wiring_servo|

* Das orangefarbene Kabel ist das Signal- und wird an GP15 angeschlossen.
* Das rote Kabel ist VCC und wird an VBUS(5V) angeschlossen.
* Das braune Kabel ist GND und wird an GND angeschlossen.

.. 1. Setzen Sie den Servoarm auf die Servo-Ausgangswelle. Bei Bedarf mit Schrauben fixieren.
.. #. Verbinden Sie **VBUS** (nicht 3V3) und GND des Pico W mit der Stromschiene des Steckbretts.
.. #. Verbinden Sie das rote Kabel des Servos mit der positiven Stromschiene mithilfe eines Jumperkabels.
.. #. Verbinden Sie das gelbe Kabel des Servos mit dem GP15-Pin mithilfe eines Jumperkabels.
.. #. Verbinden Sie das braune Kabel des Servos mit der negativen Stromschiene mithilfe eines Jumperkabels.

**Code**

.. note::

    * Öffnen Sie die Datei ``3.7_swinging_servo.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie den Code in Thonny und klicken Sie auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.

    * Vergessen Sie nicht, im unteren rechten Eck auf den Interpreter "MicroPython (Raspberry Pi Pico)" zu klicken.

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    servo = machine.PWM(machine.Pin(15))
    servo.freq(50)

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def servo_write(pin,angle):
        pulse_width=interval_mapping(angle, 0, 180, 0.5,2.5)
        duty=int(interval_mapping(pulse_width, 0, 20, 0,65535))
        pin.duty_u16(duty)

    while True:
        for angle in range(180):
            servo_write(servo,angle)
            utime.sleep_ms(20)
        for angle in range(180,-1,-1):
            servo_write(servo,angle)
            utime.sleep_ms(20)


Während das Programm läuft, sehen wir den Servoarm, der zwischen 0° und 180° hin- und herschwingt.

Das Programm wird durch die Schleife ``while True`` ständig ausgeführt, daher müssen wir den Stopp-Button drücken, um es zu beenden.

**Wie funktioniert es?**

Wir haben die Funktion ``servo_write()`` definiert, um den Servo zu steuern.

Diese Funktion hat zwei Parameter:

* ``pin``, der GPIO-Pin, der den Servo steuert.
* ``Angle``, der Ausgangswinkel der Welle.

In dieser Funktion wird ``interval_mapping()`` aufgerufen, um den Winkelbereich von 0 ~ 180 Grad auf die Pulsdauer von 0,5 ~ 2,5 ms abzubilden.

.. code-block:: python

    pulse_width=interval_mapping(angle, 0, 180, 0.5,2.5)

Warum genau 0,5 ~ 2,5 ms? Das ist durch den Arbeitsmodus des Servos bestimmt.

:ref:`Servo`

Anschließend wird die Pulsdauer von der Periode in die Tastverhältnis umgewandelt. Da ``duty_u16()`` keine Dezimalstellen akzeptiert, verwenden wir ``int()``, um das Tastverhältnis in einen Ganzzahltyp umzuwandeln.

.. code-block:: python

    duty=int(interval_mapping(pulse_width, 0, 20, 0,65535))

Schließlich wird der Tastverhältniswert in ``duty_u16()`` geschrieben.
