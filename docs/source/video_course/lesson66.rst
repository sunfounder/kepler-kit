.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 66 :  Create Your Own Libraries in Micropython
===================================================================================

This tutorial covers creating and using a Servo library with the Raspberry Pi Pico W:

* **Wiring Setup**:
 - Connect the red wire of the servo to physical pin 40 (3.3V), the brown wire to pin 38 (ground), and the orange control wire to GPIO pin 17.
* **Class and Methods**:
 - Define a `Servo` class to manage servo objects.
 - Initialize the servo with the `__init__` method, setting up the PWM pin.
 - Implement a `pos` method to control the servo's position.
* **Library Creation**:
 - Write the `Servo` class code and save it as a library file (`ServoLib.py`).
 - Create a `lib` directory on the Raspberry Pi Pico W and save the library file in this directory.
* **Code Implementation**:
 - Import necessary libraries (`machine`, `time`, and `ServoLib`).
 - Instantiate a servo object using the `Servo` class from the `ServoLib` library.
 - Control the servo's position by calling the `pos` method with desired angles.
* **Homework Assignment**:
 - Create a similar library for another component, like an LED, to streamline its usage in future projects.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/lz_Gp-zDtKI?si=VHgvS20YVqfft8LY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
