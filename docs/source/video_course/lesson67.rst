.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 67 :  Use Both Cores on Your Pi Pico with MicroPython
===================================================================================

This tutorial covers using both cores of the Raspberry Pi Pico W:

* **Wiring Setup**:
- Connect a green LED to GPIO pin 14 with a 330-ohm resistor to ground.
- Connect a red LED to GPIO pin 15 with a 330-ohm resistor to ground.
* **Code Implementation**:
- Import necessary libraries (`machine`, `time`, `_thread`).
- Set up pins for the LEDs.
- Define parameters for LED blink times.
- Create functions to control LED blinking:
   - `other_core` for the red LED on the second core.
   - `green_blink` for the green LED on the main core.
- Use `_thread.start_new_thread` to run `other_core` on the second core.
* **Homework Assignment**:
- Connect a servo.
- Control the servo and LEDs:
  - Blink red LED when servo moves backward.
  - Blink green LED when servo moves forward.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/mm1EoNqjd4c?si=RHZLX39PpGDbAFuM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
