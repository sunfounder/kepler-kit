.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 64 :  Object Oriented Programming Example in MicroPython with LEDs
===================================================================================

This tutorial covers object-oriented programming (OOP) with the Raspberry Pi Pico W, focusing on controlling LEDs:

* **Wiring Setup**:Connect a red LED to GPIO pin 15 and a green LED to GPIO pin 14, with 330-ohm resistors to the ground.
* **Class and Methods**:1. Define an `LED` class to manage LED objects.2. Initialize the LED with the `__init__` method, setting up the pin.3. Implement a `blink` method to control the blinking of the LED.
* **Code Implementation**:1. Import necessary libraries (`machine` and `time`).2. Create the `LED` class with the `__init__` and `blink` methods.3. Instantiate objects for the red and green LEDs.4. Use a loop to blink the LEDs according to specified parameters.
* **Homework Assignment**:Create a class for a Servo motor, allowing easy control of its position. The class should include methods for initializing the Servo and setting its angle. Review lesson 36 for details on working with Servo motors in MicroPython.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/3wyCL9QK_uY?si=G0GXEHqdo2jQ_F-5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
