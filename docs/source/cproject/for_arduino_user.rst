.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _projects_arduino:

Arduino-Projekte
======================

Dieser Abschnitt führt in die Arduino-Programmierung mit dem Pico W ein und zeigt Ihnen Schritt für Schritt, wie Sie die Arduino-IDE einrichten, die erforderlichen Bibliotheken installieren und spannende Projekte erstellen. Mit detaillierten Erklärungen und praktischen Übungen beherrschen Sie sowohl grundlegende als auch fortgeschrittene Arduino-basierte Hardware-Programmierung.

**Quellcode**

* :download:`SunFounder Kepler Kit <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`

* Oder schauen Sie sich den Code unter `Kepler Kit - GitHub <https://github.com/sunfounder/kepler-kit>`_ an.


1. Loslegen
------------------------

Richten Sie die Arduino-IDE ein und bereiten Sie sich darauf vor, Ihren Pico W zu programmieren. Erfahren Sie, wie Sie die IDE installieren, das Pico-W-Board konfigurieren und wichtige Bibliotheken für Ihre Projekte hinzufügen.  


.. toctree::
    :maxdepth: 1

    arduino_start/install_arduino_ide
    arduino_start/introduce_ide
    arduino_start/install_pico_w
    arduino_start/add_libraries_ar 

2. Ausgabe & Eingabe
-----------------------

Arbeiten Sie mit LEDs, Sensoren und Schaltern, um die Grundlagen der Steuerung von Ausgabegeräten und der Erfassung von Eingaben aus der physischen Welt zu erlernen. Diese grundlegenden Übungen schaffen eine solide Grundlage für die Arduino-Programmierung.  

.. toctree::
    :maxdepth: 1

    ar_led
    ar_led_bar
    ar_fade
    ar_rgb
    ar_button
    ar_tilt
    ar_slide
    ar_micro
    ar_reed
    ar_pir
    ar_pot
    ar_photoresistor
    ar_temp
    ar_water
    ar_transistor
    ar_relay

3. Sound & Anzeige & Bewegung
-------------------------------------

Erforschen Sie, wie Sie Soundeffekte erzeugen, Daten anzeigen und Bewegung steuern können. Dieses Kapitel umfasst Projekte mit Summern, NeoPixel-LEDs, LCD-Bildschirmen, Motoren, Pumpen und Servos, um Ihre Hardware zum Leben zu erwecken.  

.. toctree::
    :maxdepth: 1

    ar_ac_buz
    ar_pa_buz
    ar_neopixel
    ar_lcd
    ar_motor
    ar_pump
    ar_servo


4. Controller
---------------------

Nutzen Sie Controller wie Joysticks, Keypads und Touch-Sensoren, um Ihren Projekten interaktive Funktionen hinzuzufügen. Lernen Sie, Eingaben von diesen Geräten zu verarbeiten und in kreative Ausgaben umzusetzen.  


.. toctree::
    :maxdepth: 1

    ar_joystick
    ar_keypad
    ar_mpr121

5. Mikrochip
---------------------

Entdecken Sie die Leistungsfähigkeit von 74HC595-Schieberegistern für die fortgeschrittene LED-Steuerung, 7-Segment-Anzeigen und Punktmatrixmodule. Dieses Kapitel behandelt effiziente Techniken zum Umgang mit mehreren Ausgängen mit weniger Pins.  

.. toctree::
    :maxdepth: 1

    ar_74hc595_led
    ar_74hc595_7seg
    ar_74hc595_4dig
    ar_74hc595_matrix

6. Fortgeschritten
---------------------------------

Tauchen Sie in fortgeschrittene Module und Konzepte ein, wie z. B. die Messung von Abständen mit Ultraschall, Umweltsensorik mit DHT11, Bewegungserfassung mit MPU6050 und drahtlose Kommunikation mit RFID- und IR-Fernbedienungen.  

.. toctree::
    :maxdepth: 1

    ar_ultrasonic
    ar_dht11
    ar_mpu6050
    ar_irremote
    ar_rfid

