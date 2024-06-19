.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 69 :  Cleanly Exit MicroPython Threads When Program Terminates
===================================================================================

This tutorial covers controlling a servo and LEDs with the Raspberry Pi Pico W using both cores:

* **Wiring Setup**:
 - Connect a red LED to GPIO pin 15 with a 330-ohm resistor to ground.
 - Connect a green LED to GPIO pin 14 with a 330-ohm resistor to ground.
 - Connect the servo control wire to GPIO pin 17, power wire to physical pin 40, and ground wire to physical pin 38.
* **Code Implementation**:
 - Import necessary libraries (`machine`, `time`, `_thread`, `Servo`).
 - Set up pins for the LEDs and servo.
 - Define a function `other_core` to blink the LEDs based on the servo direction using a global variable.
 - Create a loop to move the servo and set the LED direction.
* **Homework Assignment**:
 - Extend the code to blink the red LED when the servo moves clockwise and the green LED when it moves counterclockwise.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/mcXxqx0lZYo?si=tIek_zJ4EMuZ3bC4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
