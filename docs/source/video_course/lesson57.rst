.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 57 : Calibrating a Joystick in MicroPython
=============================================================================

This tutorial covers calibrating a joystick with the Raspberry Pi Pico W:

* **Wiring Setup**: Connect ground to pin 38, 3.3V to pin 36, VRX to GPIO pin 27, and VRY to GPIO pin 26.
* **Code Implementation**: Import ``machine``, ``time``, ``math``; set up ADC for joystick axes; read and print joystick values.
* **Calibration**: Convert raw ADC values to a scale of -100 to +100, adjusting for neutral position noise.
* **Homework Assignment**: Write a program to calculate and report the angle of the joystick based on its position.




**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/rRHyho4vwIQ?si=cV75rrwEWSYoKhAN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
