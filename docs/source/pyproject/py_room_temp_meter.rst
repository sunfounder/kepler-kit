.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_room_temp:

7.2 Room Temperature Meter
======================================

Using a thermistor and an I2C LCD1602, we can create a room temperature meter.

This project is very simple, it is based on :ref:`py_temp` with I2C LCD1602 to display the temperature.


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
        - :ref:`cpn_resistor`
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_thermistor`
        - 1
        - |link_thermistor_buy|
    *   - 7
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**Schematic**

|sch_room_temp|


**Wiring**

|wiring_room_temp|

**Code**

.. note::

    * Open the ``7.2_room_temperature_meter.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.


.. code-block:: python

    from lcd1602 import LCD
    from machine import I2C, Pin
    import utime
    import math

    # Initialize the thermistor (ADC on pin 28) and LCD display
    thermistor = machine.ADC(28)  # Analog input from the thermistor

    # Initialize I2C communication for the LCD1602 display
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)

    # Create an LCD object for controlling the LCD1602 display
    lcd = LCD(i2c)

    # Main loop to continuously read temperature and display it
    while True:
        # Read raw ADC value from the thermistor
        temperature_value = thermistor.read_u16()

        # Convert the raw ADC value to a voltage (0-3.3V range)
        Vr = 3.3 * float(temperature_value) / 65535  # ADC value to voltage conversion

        # Calculate the thermistor resistance (using a voltage divider with a 10kOhm resistor)
        Rt = 10000 * Vr / (3.3 - Vr)  # Rt = thermistor resistance

        # Use the Steinhart-Hart equation to calculate the temperature in Kelvin
        # The values used are specific to the thermistor (3950 is the beta coefficient)
        temp = 1 / (((math.log(Rt / 10000)) / 3950) + (1 / (273.15 + 25)))  # Temperature in Kelvin

        # Convert temperature from Kelvin to Celsius
        Cel = temp - 273.15

        # Display the temperature on the LCD in Celsius
        string = " Temperature is \n    " + str('{:.2f}'.format(Cel)) + " C"  # Format string for the LCD
        lcd.message(string)  # Display the string on the LCD

        utime.sleep(1)  # Wait for 1 second
        lcd.clear()  # Clear the LCD for the next reading


The LCD will display the temperature value in the current environment after the program runs.

.. note:: 
    If the code and wiring are fine, but the LCD still does not display content, you can turn the potentiometer on the back to increase the contrast.
