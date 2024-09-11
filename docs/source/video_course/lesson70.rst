.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

Lesson 70:  Example of Cleanly Exiting Dual Core Program in MicroPython
===================================================================================

This tutorial covers using threading to control a servo and a button with the Raspberry Pi Pico W:

* **Wiring Setup**: Connect servo control to GPIO 17, power to pin 40, ground to pin 38. Connect button to GPIO 16 and ground.
* **Code Implementation**: Import ``machine``, ``time``, ``_thread``, ``Servo``. Set up pins for button and servo. Implement a toggle switch to control the servo's position. Use threading for servo movement and clean program exits.
* **Homework Assignment**: Modify the program to exit cleanly, even if interrupted during servo movement.



**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/UHbboCxIOYE?si=eDDi-2mYO0LSWSLJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
