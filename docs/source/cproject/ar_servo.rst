.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_servo:

3.7 - Schwingender Servo
===========================

In diesem Set gibt es neben LED und passivem Summer auch ein Gerät, das durch ein PWM-Signal gesteuert wird: der Servo.

Ein Servo ist ein Positionsservo-Gerät, das für Steuerungssysteme geeignet ist, die ständige Winkeländerungen erfordern und aufrechterhalten können. Es wird häufig in hochwertigen ferngesteuerten Spielzeugen eingesetzt, wie Flugzeugen, U-Boot-Modellen und ferngesteuerten Robotern.

Jetzt versuchen Sie, den Servo schwingen zu lassen!

* :ref:`cpn_servo`

**Benötigte Komponenten**

Für dieses Projekt benötigen wir folgende Komponenten:

Es ist sicherlich praktisch, ein komplettes Set zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM SET
        - KAUF-LINK
    *   - Kepler Kit
        - 450+
        - |link_kepler_kit|

Sie können diese auch separat über die untenstehenden Links kaufen.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTENBESCHREIBUNG
        - ANZAHL
        - KAUF-LINK

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

**Verkabelung**

|wiring_servo|

* Das orangefarbene Kabel ist das Signal und wird an GP15 angeschlossen.
* Das rote Kabel ist VCC und wird an VBUS(5V) angeschlossen.
* Das braune Kabel ist GND und wird an GND angeschlossen.

**Code**

.. note::

   * Sie können die Datei ``3.7_swinging_servo.ino`` im Pfad ``kepler-kit-main/arduino/3.7_swinging_servo`` öffnen. 
   * Oder kopieren Sie diesen Code in die **Arduino IDE**.
   * Vergessen Sie nicht, die Platine (Raspberry Pi Pico) und den richtigen Port auszuwählen, bevor Sie auf die Schaltfläche **Hochladen** klicken.

.. raw:: html

    <iframe src=https://create.arduino.cc/editor/sunfounder01/d52a67be-be6b-4cbf-b411-810160f56928/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Wenn das Programm läuft, sehen wir, wie der Servoarm sich von 0° bis 180° hin und her bewegt.

**Wie funktioniert es?**

Mit Hilfe der Bibliothek ``Servo.h`` können Sie den Servo leicht steuern.

.. code-block:: arduino

    #include <Servo.h>

**Bibliotheksfunktionen**

.. code-block:: arduino

    Servo

Erstellen Sie ein **Servo**-Objekt, um einen Servo zu steuern.

.. code-block:: arduino

    uint8_t attach(int pin); 

Verwandeln Sie einen Pin in einen Servo-Treiber. Ruft pinMode auf. Gibt 0 bei Fehler zurück.

.. code-block:: arduino

    void detach();

Gibt einen Pin vom Servo-Treiber frei.

.. code-block:: arduino

    void write(int value); 

Setzt den Winkel des Servos in Grad, von 0 bis 180.

.. code-block:: arduino

    int read();

Gibt den mit dem letzten write()-Befehl eingestellten Wert zurück.

.. code-block:: arduino

    bool attached(); 

Gibt 1 zurück, wenn der Servo aktuell angeschlossen ist.
