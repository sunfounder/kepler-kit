.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _cpn_water_level:

Water Level Sensor Module
=================================

|img_water_sensor|

The water level sensor transmits the sensed water level signal to the controller, and the computer in the controller compares the measured water level signal with the set signal to derive the deviation, and then issues "on" and "off" commands to the feedwater electric valve according to the nature of the deviation to ensure that the vessel reaches the set water level.


The water level sensor has ten exposed copper traces, five for the Power traces and five for the Sensor traces, which are crossed and bridged by water when flooded.
The circuit board has a power LED that lights up when the board is energized.

The combination of these traces acts like a variable resistor, changing the resistance value according to the water level.
To be more precise, the more water the sensor is immersed in, the better the conductivity and the lower the resistance. Conversely, the less conductive it is, the higher the resistance.
Next, the sensor will process the output signal voltage which will be sent to the microcontroller, thus helping us to determine the water level.


.. warning:: 
    The sensor cannot be fully submerged in water, please only leave the part where the ten traces are located in contact with water. In addition, energizing the sensor in a humid environment will speed up the corrosion of the probe and cut the life of the sensor, so we recommend that you only supply power when taking readings.


**Example**

* :ref:`py_water` (For MicroPython User)
* :ref:`ar_water` (For Arduino User)
* :ref:`per_water_tank` (For Piper Make User)