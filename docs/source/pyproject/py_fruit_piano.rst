.. _py_fruit_piano:

7.9 Fruit Piano
============================


Electrical conductivity is found in many metal objects, as well as in the human body and fruits.
This property can be used to create a fun little project: a fruit piano.
In other words, we turn fruits into keyboards that can play music just by touching them.

|fruit_piano|

**Bill of Materials**

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
        - Raspberry Pi Pico W
        - 1
        - |link_picow_buy|
    *   - 2
        - Micro USB Cable
        - 1
        - 
    *   - 3
        - Breadboard
        - 1
        - |link_breadboard_buy|
    *   - 4
        - Wires
        - Several
        - |link_wires_buy|
    *   - 5
        - Transistor
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - Resistor
        - 4(1-1KΩ, 1-330Ω, 2-220Ω)
        - |link_resistor_buy|
    *   - 7
        - Passive Buzzer
        - 1
        - |link_passive_buzzer_buy|
    *   - 8
        - RGB LED
        - 1
        - |link_rgb_led_buy|
    *   - 9
        - MPR121 Module
        - 1
        - 

**Schematic**

|sch_fruit_piano| 

To turn the fruit into a piano key, you still need to connect the electrodes on the MPR121 to the fruit (e.g. into the banana handle).

In the beginning, MPR121 will initialize and each electrode will get a value based on the current charge; when a conductor (such as a human body) touches an electrode, the charge will shift and rebalance.
As a result, the electrode's value is different from its initial value, telling the main control board that it has been touched.
During this process, ensure that the wiring of each electrode is stable so that its charge is balanced when initializing.


**Wiring**


|wiring_fruit_piano| 


**Code**


.. note::

    * Open the ``7.9_fruit_piano.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`. 
    
    * Here you need to use the library called ``mpr121.py``, please check if it has been uploaded to Pico W, for a detailed tutorial refer to :ref:`add_libraries_py`.


.. code-block:: python

    from mpr121 import MPR121
    from machine import Pin, I2C
    import time
    import urandom

    # mpr121
    i2c = I2C(1, sda=Pin(6), scl=Pin(7))
    mpr = MPR121(i2c)


    # buzzer
    NOTE_A3 = 220
    NOTE_B3 = 247
    NOTE_C4 = 262
    NOTE_D4 = 294
    NOTE_E4 = 330
    NOTE_F4 = 349
    NOTE_G4 = 392
    NOTE_A4 = 440
    NOTE_B4 = 494
    NOTE_C5 = 523
    NOTE_D5 = 587
    NOTE_E5 = 659

    buzzer = machine.PWM(machine.Pin(15))
    note = [NOTE_A3,NOTE_B3,NOTE_C4,NOTE_D4,NOTE_E4,NOTE_F4,NOTE_G4,NOTE_A4,NOTE_B4,NOTE_C5,NOTE_D5,NOTE_E5]

    def tone(pin,frequency):
        pin.freq(frequency)
        pin.duty_u16(30000)

    def noTone(pin):
        pin.duty_u16(0)


    # rgb led
    red = machine.PWM(machine.Pin(13))
    green = machine.PWM(machine.Pin(12))
    blue = machine.PWM(machine.Pin(11))
    red.freq(1000)
    green.freq(1000)
    blue.freq(1000)

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


    def lightup():
        red.duty_u16(int(urandom.uniform(0, 65535)))
        green.duty_u16(int(urandom.uniform(0, 65535)))
        blue.duty_u16(int(urandom.uniform(0, 65535)))


    def dark():
        red.duty_u16(0)
        green.duty_u16(0)
        blue.duty_u16(0)    

    # main project
    lastState=mpr.get_all_states()
    touchMills=time.ticks_ms()
    beat=500

    while True:
        currentState=mpr.get_all_states()
        if currentState != lastState:
            for i in range(12):
                if i in list(currentState) and not i in list(lastState):
                    tone(buzzer,note[i])
                    lightup()
                    touchMills=time.ticks_ms()
        if time.ticks_diff(time.ticks_ms(),touchMills)>=beat or len(currentState) == 0:
            noTone(buzzer)
            dark()
        lastState = currentState

Please do not touch the fruit before the program runs to avoid getting a non-correct reference during initialization.
After the program runs, touch the fruit gently, the buzzer will sound the corresponding tone and the RGB light will flash once randomly.