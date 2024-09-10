.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 71 :  Allow Thread to Complete Task Before Termination
===================================================================================

This tutorial covers gracefully terminating a multi-threaded program on the Raspberry Pi Pico W:

* **Wiring Setup**: Connect servo control to GPIO 17, power to pin 40, ground to pin 38. Connect button to GPIO 16 and ground.
* **Code Implementation**: Import ``machine``, ``time``, ``_thread``, ``Servo``. Set up pins for button and servo. Implement a toggle switch for servo movement, using threading for clean exits.
* **Handling Clean Termination**: Use a global ``running`` variable to manage loop execution. Implement a lock to control critical sections. Ensure the servo completes movement before terminating.
* **Homework Assignment**: Modify the program to handle more components or sensors, ensuring clean termination in all cases.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/Xm3chr1-hkY?si=ITIUvlqKF6UdOsq2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
