.. note::

    Ciao, benvenuto nella Community di Appassionati di Raspberry Pi & Arduino & ESP32 di SunFounder su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché Unirsi?**

    - **Supporto da Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa ai giveaway e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _projects_micropython:

Progetti MicroPython
======================

In questa sezione esplorerai i fondamenti di MicroPython, dalla sua storia all'installazione sul Pico W. Approfondirai la sintassi di base e lavorerai su numerosi progetti pratici progettati per aiutarti a padroneggiare MicroPython passo dopo passo.  

Ti consigliamo di leggere i capitoli in ordine per massimizzare la tua esperienza di apprendimento.  

**Codice Sorgente**

* :download:`SunFounder Kepler Kit <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`

* Oppure consulta il codice su `Kepler Kit - GitHub <https://github.com/sunfounder/kepler-kit>`_

1. Iniziare
------------------------
Impara i concetti di base di MicroPython e configura il tuo ambiente di sviluppo, inclusa l'installazione di Thonny, il caricamento di MicroPython sul Pico W e l'esplorazione della sua sintassi di base.  

.. toctree::
    :maxdepth: 1

    python_start/introduction_micropython
    python_start/install_thonny
    python_start/install_micropython_to_pico
    python_start/upload_libraries
    python_start/quick_guide_thonny
    python_start/syntax/micropython_basic_syntax

2. Output e Input
----------------------
Scopri come lavorare con dispositivi di output come LED e dispositivi di input come pulsanti e sensori. Questo capitolo introduce le basi della computazione fisica con progetti pratici.  

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

3. Suono, Display e Movimento
--------------------------------------
Padroneggia moduli come buzzers, LED NeoPixel, schermi LCD e attuatori come motori, pompe e servomotori. Crea progetti interattivi che producono suoni, visualizzazioni e movimento.  

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
Impara a utilizzare controller come joystick, tastiere e sensori touch per aggiungere interattività e complessità ai tuoi progetti.  

.. toctree::
    :maxdepth: 1

    py_joystick
    py_keypad
    py_mpr121

5. Microchip
--------------
Approfondisci progetti basati su microchip utilizzando i registri a scorrimento 74HC595. Controlla LED, display a 7 segmenti, matrici di punti e altro con tecniche avanzate.  

.. toctree::
    :maxdepth: 1

    py_74hc595_led
    py_74hc595_7seg
    py_74hc595_4dig
    py_74hc595_matrix

6. Avanzato
--------------------
Porta i tuoi progetti al livello successivo con componenti avanzati come sensori a ultrasuoni, moduli di temperatura e umidità DHT11, giroscopi MPU6050 e lettori RFID.  

.. toctree::
    :maxdepth: 1

    py_ultrasonic
    py_dht11
    py_mpu6050
    py_irremote
    py_rfid

7. Progetti Divertenti
----------------------
Metti in pratica le tue competenze realizzando applicazioni emozionanti e reali come theremin di luce, contatori di passeggeri, lettori musicali RFID e controller somatosensoriali. Questi progetti sono divertenti ed educativi.  

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

8. Progetti IoT
------------------------
Connetti il tuo Pico W a Internet ed esplora il mondo dell'IoT (Internet of Things). Realizza progetti come CheerLights, monitor meteorologici, sistemi di comunicazione basati su MQTT e persino un sistema di monitoraggio delle piante.  

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
