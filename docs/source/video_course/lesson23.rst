.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 23:  Temperature and Humidity Sensor with LCD Display
=============================================================================

This tutorial covers creating a temperature and humidity project using the Raspberry Pi Pico W and DHT-11 sensor with an LCD display:

* **Introduction**: introduces the tutorial, acknowledges the sponsor SunFounder, and reviews the goal of the lesson, which is to create a temperature and humidity sensor project with an LCD display.
* **Component Introduction and Setup**:
 - Describes the required components: Raspberry Pi Pico W, DHT-11 sensor, push button, and LCD 1602 display.
 - Provides a schematic and instructions for connecting these components, referring to previous lessons for detailed wiring instructions.
* **Library Installation**:
 - Guides on how to download and install the necessary library for the LCD 1602 display from toptechboy.com.
 - Provides instructions to save and import the library in Thonny IDE.
* **Code Explanation**:
 - Describes setting up the DHT-11 sensor and push button using GPIO pins.
 - Introduces a flag variable for toggling between Celsius and Fahrenheit.
 - Explains the code for reading temperature and humidity from the DHT-11 sensor.
 - Details the implementation of a toggle function to switch between Celsius and Fahrenheit.
 - Explains how to display the readings on both the console and the LCD.
* **Practical Demonstration**:
 - Shows the program in action, displaying temperature and humidity readings on the LCD.
 - Demonstrates the toggle functionality to switch between Celsius and Fahrenheit.
 - Addresses potential issues with text overlap on the LCD by adding spaces and using `LCD.clear()` to clear the screen before writing new text.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/2DZo1JeVWMk?si=mceO0XqYqT3aBpU7" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
