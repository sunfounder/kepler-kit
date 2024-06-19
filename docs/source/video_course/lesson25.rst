.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 25:  Getting Started with OLED 1306 in Micropython
=============================================================================

This tutorial covers using the Raspberry Pi Pico W and an OLED display for portable projects:

* **Introduction**:
 - Highlights the goal: continuing to untether projects from the desktop by making them portable and more power-efficient.
* **Component Review and Setup**:
 - Recaps the previous lesson: using a rechargeable LiPo battery to power the Raspberry Pi Pico W with a DHT-11 sensor, push button, and LCD display.
 - Discusses the drawbacks of using an LCD display, including higher power consumption and larger size.
* **Introducing the OLED Display**:
 - Recommends using a small, low-power, high-contrast OLED display for portable projects.
 - Shows how to connect the OLED display to the Raspberry Pi Pico W using the I2C bus, specifically on GPIO pins 2 (SDA) and 3 (SCL).
* **Library Installation and Initial Setup**:
 - Demonstrates how to install the SSD1306 library for the OLED display.
 - Explains the basic code setup, including importing necessary libraries and creating the I2C and display objects.
* **Displaying Text and Graphics**:
 - Provides code examples to display text on the OLED screen.
 - Shows how to address individual pixels and draw horizontal, vertical, and arbitrary lines.
 - Demonstrates how to create and fill rectangles on the display.
* **Power Management**:
 - Explains how to turn the display on and off to save battery power using software commands.
* **Practical Demonstration**:
 - Runs the code to show text and graphics on the OLED display.
 - Emphasizes the high contrast and low power consumption of the OLED display compared to the LCD.
* **Homework Assignment**:
 - Assigns a task: create a program that displays the title "My Circle" at the top of the screen and draws a circle with a 20-pixel radius in the center of the screen.
 - Encourages viewers to post their homework on YouTube and share the link in the comments.



**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/6SdNvqofWww?si=ZVxzi5Nm3lP5PniU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
