.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _projects_micropython:

MicroPython-Projekte
======================
In diesem Abschnitt erkunden Sie die Grundlagen von MicroPython – von seiner Geschichte bis zur Installation auf dem Pico W. Sie werden außerdem die grundlegende Syntax kennenlernen und an zahlreichen praktischen Projekten arbeiten, um MicroPython Schritt für Schritt zu meistern.  

Wir empfehlen, die Kapitel in der vorgegebenen Reihenfolge zu lesen, um das Lernerlebnis zu maximieren.  


**Quellcode**

* :download:`SunFounder Kepler Kit <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`

* Oder schauen Sie sich den Code unter `Kepler Kit - GitHub <https://github.com/sunfounder/kepler-kit>`_ an.


1. Loslegen
------------------------

Erlernen Sie die Grundlagen von MicroPython und richten Sie Ihre Entwicklungsumgebung ein, einschließlich der Installation von Thonny, dem Hochladen von MicroPython auf den Pico W und der Erkundung der grundlegenden Syntax.  


.. toctree::
    :maxdepth: 1

    python_start/introduction_micropython
    python_start/install_thonny
    python_start/install_micropython_to_pico
    python_start/upload_libraries
    python_start/quick_guide_thonny
    python_start/syntax/micropython_basic_syntax



2. Ausgabe & Eingabe
----------------------

Entdecken Sie, wie man mit Ausgabegeräten wie LEDs und Eingabegeräten wie Tastern und Sensoren arbeitet. Dieses Kapitel führt Sie in die Grundlagen des Physical Computing mit praktischen Projekten ein.  


.. toctree::
    :maxdepth: 1

    py_led
    py_led_bar
    py_fade
    py_rgb
    py_button
    py_tilt
    py_slide
    py_micro
    py_reed
    py_pir
    py_pot
    py_photoresistor
    py_temp
    py_water
    py_transistor
    py_relay

3. Sound & Anzeige & Bewegung
--------------------------------------

Meistern Sie Module wie Summer, NeoPixel-LEDs, LCD-Bildschirme und Aktuatoren wie Motoren, Pumpen und Servos. Erstellen Sie interaktive Projekte mit Sound, Visualisierungen und Bewegung.  

.. toctree::
    :maxdepth: 1

    py_ac_buz
    py_pa_buz
    py_neopixel
    py_lcd
    py_motor
    py_pump
    py_servo

4. Controller
----------------------

Lernen Sie, wie man Controller wie Joysticks, Keypads und Touch-Sensoren verwendet, um Interaktivität und Komplexität in Ihre Projekte zu integrieren.  

.. toctree::
    :maxdepth: 1

    py_joystick
    py_keypad
    py_mpr121

5. Mikrochip
--------------

Tauchen Sie in mikrochipbasierte Projekte ein, bei denen 74HC595-Schieberegister verwendet werden. Steuern Sie LEDs, 7-Segment-Anzeigen, Punktmatrizen und mehr mit fortgeschrittenen Techniken.  

.. toctree::
    :maxdepth: 1

    py_74hc595_led
    py_74hc595_7seg
    py_74hc595_4dig
    py_74hc595_matrix

6. Fortgeschritten
--------------------

Bringen Sie Ihre Projekte auf die nächste Stufe mit fortgeschrittenen Komponenten wie Ultraschallsensoren, DHT11-Temperatur- und Feuchtigkeitsmodulen, MPU6050-Gyroskopen und RFID-Lesern.  


.. toctree::
    :maxdepth: 1

    py_ultrasonic
    py_dht11
    py_mpu6050
    py_irremote
    py_rfid

7. Spaßprojekte
----------------------
Setzen Sie Ihre Fähigkeiten ein, um spannende Anwendungen wie Licht-Theremine, Passagierzähler, RFID-Musikplayer und somatosensorische Controller zu entwickeln. Diese Projekte sind unterhaltsam und lehrreich.  


.. toctree::
    :maxdepth: 1

    py_light_theremin
    py_room_temp_meter
    py_alarm_siren_lamp
    py_passenger_counter
    py_game_10_second
    py_traffic_light
    py_game_guess_number
    py_rfid_music_player
    py_fruit_piano
    py_reversing_aid
    py_somatosensory_controller
    py_digital_bubble_level

8. IoT-Projekte
------------------------
Verbinden Sie Ihren Pico W mit dem Internet und erkunden Sie die Welt des IoT (Internet der Dinge). Erstellen Sie Projekte wie CheerLights, Wettermonitore, MQTT-basierte Kommunikationssysteme und sogar ein Pflanzenüberwachungssystem.  

.. toctree::
    :maxdepth: 1

    iotproject/1.access
    iotproject/2.cheerlight
    iotproject/3.ifttt_mail
    iotproject/4.openweather
    iotproject/5.mqtt_pub
    iotproject/6.mqtt_sub
    iotproject/7.web_page
    iotproject/8.anvil
    iotproject/9.sunfounder_controller
    iotproject/10.plant_monitor
