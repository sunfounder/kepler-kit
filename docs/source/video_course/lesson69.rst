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

* **Wiring Setup**: Connect red LED to GPIO 15, green LED to GPIO 14, and servo to GPIO 17, with power to pin 40 and ground to pin 38.
* **Code Implementation**: Import ``machine``, ``time``, ``_thread``, and ``Servo``. Set up pins for LEDs and servo. Define ``other_core`` to blink LEDs based on servo movement. Create loop to control servo and LEDs.
* **Homework Assignment**: Modify the code to blink red LED for clockwise and green LED for counterclockwise servo movement.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/mcXxqx0lZYo?si=tIek_zJ4EMuZ3bC4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
