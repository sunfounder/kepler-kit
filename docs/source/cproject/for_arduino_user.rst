.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino e ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni festive e concorsi a premi.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _projects_arduino:

Progetti Arduino
======================

Questa sezione introduce la programmazione Arduino con il Pico W, guidandoti attraverso il processo di configurazione dell'IDE di Arduino, l'installazione delle librerie necessarie e la realizzazione di progetti entusiasmanti. Con spiegazioni dettagliate ed esercizi pratici, padroneggerai sia la programmazione hardware Arduino di base che quella avanzata.

**Codice Sorgente**

* :download:`SunFounder Kepler Kit <https://github.com/sunfounder/kepler-kit/archive/refs/heads/main.zip>`

* Oppure consulta il codice su `Kepler Kit - GitHub <https://github.com/sunfounder/kepler-kit>`_

1. Iniziare
------------------------
Configura l'IDE di Arduino e preparati a programmare il tuo Pico W. Impara come installare l'IDE, configurare la scheda Pico W e aggiungere le librerie essenziali per i tuoi progetti.  

.. toctree::
    :maxdepth: 1

    arduino_start/install_arduino_ide
    arduino_start/introduce_ide
    arduino_start/install_pico_w
    arduino_start/add_libraries_ar 

2. Output e Input
-----------------------
Lavora con LED, sensori e interruttori per apprendere le basi del controllo dei dispositivi di output e della raccolta di input dal mondo fisico. Questi esercizi fondamentali ti daranno una solida base nella programmazione Arduino.  

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

3. Suono, Display e Movimento
-------------------------------------
Scopri come creare effetti sonori, visualizzare dati e controllare il movimento. Questo capitolo include progetti con buzzers, LED NeoPixel, schermi LCD, motori, pompe e servomotori per dare vita al tuo hardware.  

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
Utilizza controller come joystick, tastiere e sensori touch per aggiungere funzionalità interattive ai tuoi progetti. Impara a elaborare gli input di questi dispositivi e tradurli in output creativi.  

.. toctree::
    :maxdepth: 1

    ar_joystick
    ar_keypad
    ar_mpr121

5. Microchip
---------------------
Scopri la potenza dei registri a scorrimento 74HC595 per il controllo avanzato dei LED, dei display a 7 segmenti e dei moduli a matrice di punti. Questo capitolo copre tecniche efficienti per gestire più output con meno pin.  

.. toctree::
    :maxdepth: 1

    ar_74hc595_led
    ar_74hc595_7seg
    ar_74hc595_4dig
    ar_74hc595_matrix

6. Avanzato
----------------
Approfondisci moduli e concetti avanzati, come la misurazione delle distanze con ultrasuoni, il rilevamento ambientale con DHT11, il monitoraggio del movimento con MPU6050 e la comunicazione wireless con RFID e telecomandi IR.  

.. toctree::
    :maxdepth: 1

    ar_ultrasonic
    ar_dht11
    ar_mpu6050
    ar_irremote
    ar_rfid
