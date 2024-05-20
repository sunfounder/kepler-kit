.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_motor:

3.5 Small Fan
=======================


Now we use the TA6586 to drive the DC motor to make it rotate clockwise and counterclockwise. 
Since the DC motor requires a relatively large current, for safety reasons, 
here we use a power module to supply power to the motor.

* :ref:`cpn_motor`
* :ref:`cpn_ta6586`
* :ref:`cpn_power_module`

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
        - :ref:`cpn_ta6586`
        - 1
        - 
    *   - 6
        - :ref:`cpn_motor`
        - 1
        - |link_motor_buy| 
    *   - 7
        - :ref:`cpn_lipo_charger`
        - 1
        -  
    *   - 8
        - 18650 Battery
        - 1
        -  
    *   - 9
        - Battery Holder
        - 1
        -  



**Schematic**

|sch_motor|



**Wiring**

.. note::

    * Since DC motors require a high current, we use a Li-po Charger module to power the motor here for safety reasons.
    * Make sure your Li-po Charger Module is connected as shown in the diagram. Otherwise, a short circuit will likely damage your battery and circuitry.


|wiring_motor|


**Code**

.. note::

    * Open the ``3.5_small_fan.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    motor1A = machine.Pin(14, machine.Pin.OUT)
    motor2A = machine.Pin(15, machine.Pin.OUT)

    def clockwise():
        motor1A.high()
        motor2A.low()

    def anticlockwise():
        motor1A.low()
        motor2A.high()

    def stopMotor():
        motor1A.low()
        motor2A.low()

    while True:
        clockwise()
        utime.sleep(1)
        stopMotor()
        utime.sleep(1)
        anticlockwise()
        utime.sleep(1)
        stopMotor()
        utime.sleep(1)


Once the program is running, the motor will rotate back and forth in a regular pattern.


.. note::

    * If the motor is still spinning after you click the Stop button, you need to reset the **RUN** pin on the Pico W with a wire to GND at this time, and then unplug this wire to run the code again.
    * This is because the motor is operating with too much current, which may cause the Pico W to disconnect from the computer. 

    |wiring_run_reset|