.. _py_traffic_light:


7.6 Traffic Light
=================================


`Traffic Light <https://en.wikipedia.org/wiki/Traffic_light>`_ is a signal device located at roadway intersections, crosswalks and other locations to control the flow of traffic.

Traffic signals are standardized by the `Vienna Convention on Road Signs and Signals <https://en.wikipedia.org/wiki/Vienna_Convention_on_Road_Signs_and_Signals>`_.
Provides users with the right-of-way by alternating LEDs in three standard colors.

* **Red light**: Traffic should stop if it sees a flashing red light, equivalent to a stop sign.
* **Yellow light**: A warning signal is about to turn red. Yellow lights are interpreted differently in different countries (regions).
* **Green light**: Allows traffic to move in the indicated direction.

In this project, we will use three colors of LEDs to implement traffic light changes and a 4-digit 7-segment display to show the time of each traffic state.

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
        - 7(220Ω)
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
        - LED
        - 1
        - |link_led_buy|


**Schematic**


|sch_traffic_light|


* This circuit is based on the :ref:`py_74hc_4dig` with the addition of 3 LEDs.
* The 3 red, yellow and green LEDs are connected to GP7~GP9 respectively.

**Wiring**


|wiring_traffic_light| 


**Code**

.. note::

    * Open the ``7.6_traffic_light.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time
    from machine import Timer

    # [Green, Yellow, Red]
    lightTime=[30, 5, 30]

    # display
    SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

    sdi = machine.Pin(18,machine.Pin.OUT)
    rclk = machine.Pin(19,machine.Pin.OUT)
    srclk = machine.Pin(20,machine.Pin.OUT)

    placePin = []
    pin = [10,13,12,11]
    for i in range(4):
        placePin.append(None)
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)

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

    def display(num):
        
        pickDigit(0)
        hc595_shift(SEGCODE[num%10])

        pickDigit(1)
        hc595_shift(SEGCODE[num%100//10])
        
        pickDigit(2)
        hc595_shift(SEGCODE[num%1000//100])
        
        pickDigit(3)
        hc595_shift(SEGCODE[num%10000//1000])    

    # led
    # 9Red, 8Yellow,7Green
    pin = [7,8,9]
    led=[]
    for i in range(3):
        led.append(None)
        led[i] = machine.Pin(pin[i], machine.Pin.OUT)

    def lightup(state):
        for i in range(3):
            led[i].value(0)
        led[state].value(1)

    # timer
    counter = 0
    color_state= 0

    def time_count(ev):
        global counter, color_state
        counter -= 1
        if counter <= 0:
            color_state = (color_state+1) % 3
            counter = lightTime[color_state]
            
    tim = Timer(period=1000, mode=Timer.PERIODIC, callback=time_count)


    while True:
        display(counter)
        lightup(color_state)

When the code runs, the green LED stays on for 30 seconds, the yellow LED stays on for 5 seconds, and the green LED stays on for 30 seconds.