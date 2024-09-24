

.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_reversing_aid:

7.10 Reversing Aid
======================

This project uses an LED, a buzzer and an ultrasonic module to create a reversing assist system.
We can put it on a remote control car to simulate the the actual process of reversing a car into a garage.


**Required Components**

In this project, we need the following components. 

It's definitely convenient to buy a whole kit, here's the link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ITEMS IN THIS KIT
        - LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|

You can also buy them separately from the links below.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENT	
        - QUANTITY
        - LINK

    *   - 1
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Micro USB Cable
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Several
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 2(1KΩ, 220Ω)
        - |link_resistor_buy|
    *   - 7
        - Active :ref:`cpn_buzzer`
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

**Schematic**

|sch_reversing_aid|


**Wiring**

|wiring_reversing_aid| 

**Code**

.. note::

    * Open the ``7.10_reversing_aid.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.



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


* As soon as the program runs, the ultrasonic sensor will continuously read the distance to the obstacle in front of you, and you will be able to see the exact distance value on the shell.
* The LED and buzzer will change the frequency of blinking and beeping depending on the distance value, thus indicating the approach of the obstacle.
* The :ref:`py_ultrasonic` article mentioned that when the ultrasonic sensor works, the program will be paused.
* To avoid interfering with the LED or buzzer timing, we created a separate thread for ranging in this example.

