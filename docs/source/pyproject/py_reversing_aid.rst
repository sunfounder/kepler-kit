

.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_reversing_aid:

7.10 Einparkhilfe
======================

Dieses Projekt nutzt eine LED, einen Summer und ein Ultraschallmodul, um ein Einparkassistenzsystem zu realisieren. Es lässt sich auf ein ferngesteuertes Auto setzen, um den realen Vorgang des Einparkens in eine Garage zu simulieren.

**Benötigte Komponenten**

Für dieses Projekt werden die folgenden Komponenten benötigt.

Es ist definitiv praktisch, ein ganzes Set zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Bezeichnung	
        - IN DIESEM SET ENTHALTENE ARTIKEL
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
        - :ref:`cpn_transistor`
        - 1 (S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 2 (1KΩ, 220Ω)
        - |link_resistor_buy|
    *   - 7
        - Aktiver :ref:`cpn_buzzer`
        - 1
        -
    *   - 8
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 9
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**Schaltplan**

|sch_reversing_aid|

**Verkabelung**

|wiring_reversing_aid| 

**Code**

.. note::

    * Öffnen Sie die Datei ``7.10_reversing_aid.py`` im Verzeichnis ``kepler-kit-main/micropython`` oder kopieren Sie diesen Code in Thonny und klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie einfach F5.
  
    * Vergessen Sie nicht, im unteren rechten Eck den Interpreter "MicroPython (Raspberry Pi Pico)" auszuwählen.

    * Für detaillierte Anleitungen siehe :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

    # Initialize pins for the buzzer and LED
    buzzer = machine.Pin(15, machine.Pin.OUT)  # Buzzer on pin 15
    led = machine.Pin(14, machine.Pin.OUT)  # LED on pin 14

    # Initialize pins for the ultrasonic sensor (HC-SR04)
    TRIG = machine.Pin(17, machine.Pin.OUT)  # Trigger pin for the ultrasonic sensor
    ECHO = machine.Pin(16, machine.Pin.IN)  # Echo pin for the ultrasonic sensor

    dis = 100  # Global variable to store the distance

    # Function to measure distance using the ultrasonic sensor
    def distance():
        TRIG.low()
        time.sleep_us(2)
        TRIG.high()
        time.sleep_us(10)
        TRIG.low()

        timeout_start = time.ticks_us()  # Use microseconds for more precision
        
        # Wait for ECHO pin to go high (start of echo pulse)
        while not ECHO.value():
            if time.ticks_diff(time.ticks_us(), timeout_start) > 30000:  # 30ms timeout
                return -1  # Timeout, return -1 if no pulse is detected
        
        time1 = time.ticks_us()  # Start time for pulse width calculation
        
        # Wait for ECHO pin to go low (end of echo pulse)
        while ECHO.value():
            if time.ticks_diff(time.ticks_us(), time1) > 30000:  # 30ms timeout
                return -1  # Timeout, return -1 if pulse is too long
        
        time2 = time.ticks_us()  # End time for pulse width calculation
        
        # Calculate the distance based on the duration of the echo pulse
        during = time.ticks_diff(time2, time1)
        distance_cm = during * 340 / 2 / 10000  # Convert time to distance in cm
        return distance_cm

    # Function to beep the buzzer and light up the LED
    def beep():
        buzzer.value(1)  # Turn on the buzzer
        led.value(1)  # Turn on the LED
        time.sleep(0.1)  # Beep duration
        buzzer.value(0)  # Turn off the buzzer
        led.value(0)  # Turn off the LED
        time.sleep(0.1)  # Short pause between beeps

    # Initialize variables for controlling beep intervals
    intervals = 2000  # Default long initial interval
    previousMillis = time.ticks_ms()  # Store the previous time to track beep intervals

    # Main loop to handle distance-based beeping intervals
    while True:
        dis = distance()  # Measure the distance directly in the main loop

        # Adjust beep intervals based on the distance
        if dis > 0:  # Ensure valid distance is measured
            if dis <= 10:
                intervals = 300  # Close distance, faster beeps
            elif dis <= 20:
                intervals = 500  # Medium-close distance, moderate beeps
            elif dis <= 50:
                intervals = 1000  # Medium distance, slower beeps
            else:
                intervals = 2000  # Far distance, much slower beeps

            # Print the measured distance
            print(f'Distance: {dis:.2f} cm')
            
            # Check if it's time to beep again based on the interval
            currentMillis = time.ticks_ms()  # Get the current time
            if time.ticks_diff(currentMillis, previousMillis) >= intervals:
                beep()  # Beep the buzzer and blink the LED
                previousMillis = currentMillis  # Update the time of the last beep
            
        time.sleep_ms(100)  # Small delay to avoid too frequent readings



* Sobald das Programm läuft, wird der Ultraschallsensor kontinuierlich die Entfernung zum vor Ihnen befindlichen Hindernis messen, und Sie können den genauen Entfernungswert in der Shell sehen.
* Je nach Entfernungswert ändern die LED und der Summer die Frequenz ihres Blinkens und Piepsens und signalisieren so die Annäherung an das Hindernis.
* Im Artikel :ref:`py_ultrasonic` wurde erwähnt, dass das Programm pausiert, während der Ultraschallsensor arbeitet.
* Um die Timing von LED und Summer nicht zu beeinträchtigen, haben wir in diesem Beispiel einen separaten Thread für die Entfernungsmessung erstellt.

