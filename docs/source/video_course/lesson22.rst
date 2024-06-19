.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 22:  Using an LCD Display with the Pico W
=============================================================================

This tutorial covers connecting and using an LCD 1602 display with the Raspberry Pi Pico W:

* **Introduction**: introduces the tutorial, acknowledges the sponsor SunFounder, and explains the goal of adding an LCD display to the Raspberry Pi Pico W project for mobile use.

* **Component Introduction and Setup**:
- Describes the required components: LCD 1602 display and female-to-male wires.
- Details the connections:
  - LCD 1602 pins to Raspberry Pi Pico W:
    - Ground to pin 38
    - VCC (5V) to the rightmost pin
    - SDA (data) to GPIO pin 6
    - SCL (clock) to GPIO pin 7

* **Library Installation**:
 - Guides on how to download and install the necessary library for the LCD 1602 display from toptechboy.com.
 - Provides instructions to save and import the library in Thonny IDE.

* **Code Explanation**:
 - Describes the creation of an LCD object and writing text to the LCD.
 - Provides a sample program that prompts for the user’s name and displays a greeting message on the LCD.
 - Addresses potential issues with text overlap by using `LCD.clear()` to clear the screen before writing new text.

* **Practical Demonstration**:
 - Shows the program in action, displaying names on the LCD.
 - Explains adjusting the LCD contrast using a potentiometer on the back of the display.

* **Homework Assignment**:
 - Assigns a task to integrate the LCD display with the DHT11 temperature and humidity sensor project from lesson 21.
 - Instructs to display temperature in Celsius or Fahrenheit based on a toggle button and display humidity on the LCD.



**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/liwMc01LOIA?si=ZRpzb2YskRgxd3Kn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

