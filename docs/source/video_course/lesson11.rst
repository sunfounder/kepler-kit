.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 12:  Understanding and Controlling an RGB LED in MicroPython
==========================================================================

This tutorial covers controlling an RGB LED using the SunFounder Kepler Kit and Raspberry Pi Pico W:

* **RGB LED Control**: Explains controlling RGB LED colors using PWM (Pulse Width Modulation). Discusses the structure of the RGB LED, which has three LEDs (red, green, and blue) with a common ground. Emphasizes the importance of using separate current-limiting resistors for each color channel to prevent crosstalk.
* **Wiring Diagram and Setup**: Provides a detailed wiring diagram for connecting the RGB LED and the required resistors to the Raspberry Pi Pico W. Demonstrates the physical setup on a breadboard, including connections for red, green, and blue channels to GPIO pins 13, 14, and 15, respectively.
* **Code Explanation**: Describes the code for setting up PWM on each GPIO pin and controlling the brightness of each color channel. Covers the setup of PWM frequency, duty cycle, and the initialization of GPIO pins for red, green, and blue channels.
* **Practical Demonstration**: Shows how to run the code to change the color of the RGB LED. Demonstrates turning individual color channels on and off, and adjusting brightness levels.
* **Homework Assignment**: Asks users to create a program that prompts the user for a color (red, green, blue, cyan, magenta, yellow, orange, or white) and adjusts the RGB LED to display the specified color. Encourages users to mix and match PWM values to achieve accurate color representation.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/yZkx-KWbATY?si=p85rQXYb6YGoEe9L" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

