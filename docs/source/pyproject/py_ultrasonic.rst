.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_ultrasonic:

6.1 Measuring Distance
======================================

The ultrasonic sensor module works on the principle of sonar and radar systems for determining the distance to an object.

* :ref:`cpn_ultrasonic`

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
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|


**Schematic**

|sch_ultrasonic|

**Wiring**

|wiring_ultrasonic|

**Code**

.. note::

    * Open the ``6.1_measuring_distance.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import time

    TRIG = machine.Pin(17,machine.Pin.OUT)
    ECHO = machine.Pin(16,machine.Pin.IN)

    def distance():
        TRIG.low()
        time.sleep_us(2)
        TRIG.high()
        time.sleep_us(10)
        TRIG.low()
        while not ECHO.value():
            pass
        time1 = time.ticks_us()
        while ECHO.value():
            pass
        time2 = time.ticks_us()
        during = time.ticks_diff(time2,time1)
        return during * 340 / 2 / 10000

    while True:
        dis = distance()
        print ('Distance: %.2f' % dis)
        time.sleep_ms(300)

Once the program is running, the Shell will print out the distance of the ultrasonic sensor from the obstacle ahead.

**How it works?**

Ultrasonic sensors produce high frequency sound waves (ultrasonic waves) emitted by the transmitting probe. When this ultrasonic wave hits an object, it is reflected as an echo, which is detected by the receiving probe. By calculating the time from transmission to reception, the distance can be calculated.
Based on this principle, the function ``distance()`` can be derived.

.. code-block:: python

    def distance():
        TRIG.low()
        time.sleep_us(2)
        TRIG.high()
        time.sleep_us(10)
        TRIG.low()
        while not ECHO.value():
            pass
        time1 = time.ticks_us()
        while ECHO.value():
            pass
        time2 = time.ticks_us()
        during = time.ticks_diff(time2,time1)
        return during * 340 / 2 / 10000

* Among them, the first few lines are used to transmit a 10us ultrasonic wave.

.. code-block:: python

    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()

* Then, the program is paused and the current time is recorded when the ultrasonic wave has been emitted.

.. code-block:: python

        while not ECHO.value():
            pass
        time1 = time.ticks_us()

* Subsequently, the program is suspended again. After the echo is received, the current time is recorded once again.

.. code-block:: python

        while ECHO.value():
            pass
        time2 = time.ticks_us()

* Finally, based on the time difference between the two recordings, the speed of sound (340m/s) is multiplied by the time to obtain double the distance between the ultrasonic module and the obstacle (i.e., one round trip of the ultrasonic waves from the module to the obstacle). Converting the units to centimeters gives us the return value we need.

.. code-block:: python

        during = time.ticks_diff(time2,time1)
        return during * 340 / 2 / 10000

Note that the ultrasonic sensor will pause the program when it is working, which may cause some lagging when writing complex projects.

