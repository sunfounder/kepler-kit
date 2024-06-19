.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 65 :  Create a Servo Class and Method in MicroPython
===================================================================================

This tutorial covers creating a Servo class using object-oriented programming (OOP) with the Raspberry Pi Pico W:

* **Wiring Setup**:
Connect the red wire of the servo to physical pin 40 (3.3V), the brown wire to pin 38 (ground), and the orange control wire to GPIO pin 17.
* **Class and Methods**:
 - Define a `Servo` class to manage servo objects.
 - Initialize the servo with the `__init__` method, setting up the PWM pin.
 - Implement a `pos` method to control the servo's position.
* **Code Implementation**:
 - Import necessary libraries (`machine` and `time`).
 - Create the `Servo` class with the `__init__` and `pos` methods.
 - Instantiate a servo object and control its position using the `pos` method.
* **Homework Assignment**:
 - Review lesson 36 for details on working with servos. Create a Servo class that allows easy control of the servo's position by setting angles. Implement a method to move the servo based on user input.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/OI4MzX7zqGc?si=ReJ76mhOZqUdnL9h" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
