.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 68 :  MicroPython Multicore Threading Example with LEDs and Servo
===================================================================================

This tutorial covers controlling a servo and LEDs with the Raspberry Pi Pico W using both cores:

* **Wiring Setup**: Connect red LED to GPIO 15, green LED to GPIO 14, servo to GPIO 17, power to pin 40, and ground to pin 38.
* **Code Implementation**: Import ``machine``, ``time``, ``_thread``, and ``Servo``. Set up pins for LEDs and servo. Define ``other_core`` function to blink LEDs based on servo direction.
* **Homework Assignment**: Modify code to blink red LED for clockwise and green LED for counterclockwise servo movement.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/n2eQTw9axHg?si=TRVLEM1EqyD_DefA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
