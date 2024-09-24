.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_alarm_lamp:

7.3 Alarm Siren Lamp
=======================

Police lights are often visible in real life (or in movies). Usually, it is used to maintain traffic, serve as a warning device, and serve as an important safety prop for officers, emergency vehicles, fire trucks, and engineering vehicles. When you see its lights or hear its sound, you must be careful, which means you (or those around you) may be in danger.

An LED and buzzer are used here to create a small warning light, which is activated by a slide switch.

|sirem_alarm|


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
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 6
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 7
        - :ref:`cpn_resistor`
        - 3(1KΩ, 220Ω, 10KΩ)
        - |link_resistor_buy|
    *   - 8
        - Passive :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 9
        - :ref:`cpn_capacitor`
        - 1(104)
        - |link_capacitor_buy|
    *   - 10
        - :ref:`cpn_slide_switch`
        - 1
        - 


**Schematic**

|sch_alarm_siren_lamp|

* GP17 is connected to the middle pin of the slider, along with a 10K resistor and a capacitor (filter) in parallel to GND, which allows the slider to output a steady high or low level when toggled to the left or right.
* As soon as GP15 is high, the NPN transistor conducts, causing the passive buzzer to start sounding. This passive buzzer is programmed to gradually increase in frequency to produce a siren sound.
* An LED is connected to GP16 and is programmed to periodically change its brightness in order to simulate a siren.



**Wiring**

|wiring_alarm_siren_lamp|


**Code**

.. note::

    * Open the ``7.3_alarm_siren_lamp.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import time

    # Initialize the PWM for the buzzer (on pin 15) and LED (on pin 16)
    buzzer = machine.PWM(machine.Pin(15))  # PWM for buzzer
    led = machine.PWM(machine.Pin(16))  # PWM for LED
    led.freq(1000)  # Set the frequency of the LED PWM to 1kHz

    # Initialize the switch (on pin 17) as an input pin
    switch = machine.Pin(17, machine.Pin.IN)

    # Function to stop the buzzer by setting the duty cycle to 0%
    def noTone(pin):
        pin.duty_u16(0)  # Set the PWM duty cycle to 0, stopping the sound

    # Function to play a tone on the buzzer with a specified frequency
    def tone(pin, frequency):
        pin.freq(frequency)  # Set the frequency for the buzzer
        pin.duty_u16(30000)  # Set duty cycle to around 50% (30000 out of 65535)

    # Function to map a value from one range to another
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    # Interrupt handler function to toggle the bell_flag when the switch is pressed
    def toggle(pin):
        global bell_flag
        bell_flag = not bell_flag  # Toggle the bell_flag value
        print(bell_flag)  # Print the current state of bell_flag for debugging
        
        # Change the switch interrupt depending on the state of the bell_flag
        if bell_flag:
            # If bell_flag is True, listen for a falling edge (when switch is released)
            switch.irq(trigger=machine.Pin.IRQ_FALLING, handler=toggle)
        else:
            # If bell_flag is False, listen for a rising edge (when switch is pressed)
            switch.irq(trigger=machine.Pin.IRQ_RISING, handler=toggle)

    # Initialize bell_flag to False (buzzer and LED off by default)
    bell_flag = False

    # Set up an interrupt to detect when the switch is pressed (rising edge)
    switch.irq(trigger=machine.Pin.IRQ_RISING, handler=toggle)

    # Main loop to control the buzzer and LED based on the bell_flag
    while True:
        if bell_flag == True:
            # If bell_flag is True, gradually increase the brightness of the LED
            # and change the buzzer frequency to simulate a bell ringing effect
            for i in range(0, 100, 2):  # Loop from 0 to 100 in steps of 2
                led.duty_u16(int(interval_mapping(i, 0, 100, 0, 65535)))  # Map i to LED brightness
                tone(buzzer, int(interval_mapping(i, 0, 100, 130, 800)))  # Map i to buzzer frequency
                time.sleep_ms(10)  # Short delay to create a smooth ramp
        else:
            # If bell_flag is False, stop the buzzer and turn off the LED
            noTone(buzzer)  # Stop the buzzer
            led.duty_u16(0)  # Turn off the LED (set duty cycle to 0)


Once the program is running, toggle the slide switch to the left (yours may be to the right, depending on how your slide switch is wired) and the buzzer will emit a progressive warning tone and the LED will change its brightness accordingly; toggle the slide switch to the right and the buzzer and LED will stop working.