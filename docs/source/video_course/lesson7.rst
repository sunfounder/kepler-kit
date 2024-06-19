.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 7:  Controlling 3 LED with a Potentiometer in Micropython
====================================================================

This tutorial covers using a potentiometer to control three LEDs (green, yellow, and red) with the Raspberry Pi Pico W:

* **Homework Solution Review**: Recaps the previous assignment to connect a potentiometer and three LEDs, and map the potentiometer readings from 0 to 100 to control the LEDs based on the input values.
* **Circuit Setup**: Provides a detailed wiring diagram and setup for connecting the potentiometer and LEDs to the Raspberry Pi Pico W. Includes creating ground and 3.3V rails, and connecting the components to the appropriate GPIO pins.
* **Reading and Mapping Potentiometer Values**: Demonstrates how to read analog values from the potentiometer and map them from their original range (432 to 65,535) to a 0 to 100 scale using mathematical equations.
* **Conditional Logic for LED Control**: Implements if statements to control the LEDs based on the potentiometer readings:Green LED for values between 0 and 79.Yellow LED for values between 80 and 94.Red LED for values between 95 and 100.
* **Practical Demonstration**: Shows the working circuit and code in action, with the LEDs lighting up based on the potentiometer's position.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/YqvcSnGd_HQ?si=igsP6I-k3FhYA7Go" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

