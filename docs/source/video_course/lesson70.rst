.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 70 :  Example of Cleanly Exiting Dual Core Program in MicroPython
===================================================================================

This tutorial covers using threading to control a servo and a button with the Raspberry Pi Pico W:

* **Wiring Setup**:

- Connect the servo's control wire to GPIO pin 17, power wire to physical pin 40, and ground wire to physical pin 38.
- Connect a button to GPIO pin 16 and ground.

* **Code Implementation**:

 - Import necessary libraries (`machine`, `time`, `_thread`, `Servo`).
 - Set up pins for the button and servo.
 - Implement a toggle switch for the button to control the servo's movement.
 - Define a main loop to detect button presses and toggle the servo between 0 and 180 degrees.
 - Use threading to handle the servo movement on a separate core, allowing for clean program exits.

* **Homework Assignment**:

 - Modify the program to ensure it exits cleanly even if interrupted while the servo is moving.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/UHbboCxIOYE?si=eDDi-2mYO0LSWSLJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
