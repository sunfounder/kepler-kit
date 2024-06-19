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

* **Wiring Setup**:
  - Connect the servo's control wire to GPIO pin 17, power wire to physical pin 40, and ground wire to physical pin 38.
  - Connect a button to GPIO pin 16 and ground.
* **Code Implementation**:
  - Import necessary libraries (`machine`, `time`, `_thread`, `Servo`).
  - Set up pins for the button and servo.
  - Implement a toggle switch for the button to control the servo's movement.
  - Define a main loop to detect button presses and toggle the servo between 0 and 180 degrees.
  - Use threading to handle the servo movement on a separate core, allowing for clean program exits.
* **Handling Clean Termination**:
  - Use a global `running` variable to control the loop execution.
  - Implement a baton (lock) to ensure only one part of the program runs at a time during critical sections.
  - Wait for the servo movement to complete before terminating the program.
* **Homework Assignment**:
  - Modify the program to handle additional components or sensors, ensuring clean termination in all scenarios.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/Xm3chr1-hkY?si=ITIUvlqKF6UdOsq2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
