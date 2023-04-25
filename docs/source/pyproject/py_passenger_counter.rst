.. _py_passage_counter:


7.4 Passenger Counter
==============================

For large shopping malls, shopping centers, chain stores, airports, stations, museums, and public places such as exhibition halls, passenger traffic is an indispensable data.

In airports and stations, for example, the number of people needs to be strictly controlled to ensure safety and smooth flow.
It is also possible to know when there are more visitors in shopping centers and chain stores, how many orders each user can generate, etc.
As a result, we can analyze people's consumption habits and increase turnover.

Passenger counters can help people understand the operation of these public places and organize their operations efficiently.

A simple passenger counter is created using a PIR sensor and a 4-digit 7-segment display.


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
        - Resistor
        - 4(220Ω)
        - |link_resistor_buy|
    *   - 6
        - 4-Digit 7 Segment Display
        - 1
        - 
    *   - 7
        - 74HC595
        - 1
        - |link_74hc595_buy|
    *   - 8
        - PIR Module
        - 1
        - |link_pir_buy|

**Schematic**

|sch_passager_counter| 

* This circuit is based on the :ref:`py_74hc_4dig` with the addition of a PIR module.
* The PIR will send a high signal of about 2.8s long when someone passes by.
* The PIR module has two potentiometers: one adjusts sensitivity, the other adjusts detection distance. To make the PIR module work better, you need to turn both of them counterclockwise to the end.

    |img_PIR_TTE|


**Wiring**


|wiring_passager_counter| 


**Code**

.. note::

    * Open the ``7.4_passenger_counter.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import time


    pir_sensor = machine.Pin(16, machine.Pin.IN)

    SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

    sdi = machine.Pin(18,machine.Pin.OUT)
    rclk = machine.Pin(19,machine.Pin.OUT)
    srclk = machine.Pin(20,machine.Pin.OUT)

    placePin = []
    pin = [10,13,12,11]
    for i in range(4):
        placePin.append(None)
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)

    count = 0


    def pickDigit(digit):
        for i in range(4):
            placePin[i].value(1)
        placePin[digit].value(0)

    def clearDisplay():
        hc595_shift(0x00)

    def hc595_shift(dat):
        rclk.low()
        time.sleep_us(200)
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_us(200)
            value = 1 & (dat >> bit)
            sdi.value(value)
            time.sleep_us(200)
            srclk.high()
            time.sleep_us(200)
        time.sleep_us(200)
        rclk.high()

    def motion_detected(pin):
        global count
        count = count+1

    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)

    while True:
        #print(count)
        
        pickDigit(0)
        hc595_shift(SEGCODE[count%10])

        pickDigit(1)
        hc595_shift(SEGCODE[count%100//10])
        
        pickDigit(2)
        hc595_shift(SEGCODE[count%1000//100])
        
        pickDigit(3)
        hc595_shift(SEGCODE[count%10000//1000])


When the code is run, the number on the 4-digit 7-segment display will be added by one if someone passes in front of the PIR module.

