.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _cpn_lipo_charger:

Li-po Charger Module
=================================================


|lipo_module|

This is a Li-po charger module designed for Raspberry Pi Pico/Pico H/Pico W. Just plug it and the Pico into the breadboard as shown below, and then connect the battery at the other end and you are ready to use.

When you plug in the Pico W with a USB cable connected to a computer or socket, the indicator light on the Li-po Charger module lights up, representing the battery will be charged at the same time. When you unplug the USB cable, the Pico W will be powered by the battery, so you can keep your project running.


.. note::
    For some computers with poor performance, sometimes if you plug in your Pico W to your computer with this charging module attached, it may cause the computer not to recognize your Pico W.

    The reason is that after plugging in, while charging the battery, the USB port voltage is pulled down, resulting in the Pico W power supply is insufficient to be recognized by the computer.
    
    In this case, you need to pull out the Li-Po charging module and then plug in the Pico W again.

|lipo_wire|

**Features**

* Input voltage: 5V
* Output voltage: 3.3V
* Size: 20mmx7mm
* Interface model: PH2.0
* There is a matching 1A battery holder as well as an 800mAh 18650 used together.


**Schematic**

|sch_lipo_charger|