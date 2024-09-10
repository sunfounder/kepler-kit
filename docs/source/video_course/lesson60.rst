.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 60 : Control NeoPixel Colors with a Joystick in MicroPython
=============================================================================

This tutorial covers controlling an LED strip with a joystick using the Raspberry Pi Pico W:

* **Wiring Setup**:

    - Connect joystick ground to pin 38, 3.3V to pin 36, VRX to GPIO pin 27, VRY to GPIO pin 26. 
    - Connect Neopixel ground to pin 38, 5V to pin 40, data to GPIO pin 0.
    
* **Code Implementation**: 

    - Import libraries (``machine``, ``time``, ``math``, ``neopixel``). 
    - Set up ADC for joystick and Neopixel. Read joystick values, calculate angles. 
    - Convert angles to RGB for Neopixel.

* **Homework Assignment**: Write a program to control Neopixel color and brightness based on joystick angle and distance from center.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/8UCJHY7uTH4?si=BKJ8lYNz1kF4w9wm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
