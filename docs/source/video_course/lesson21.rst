.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 21:  Temperature and Humidity Measurements with Toggle Switch
=============================================================================

This tutorial covers adding a toggle push button to switch between temperature readings in Fahrenheit and Celsius using the DHT11 sensor with the Raspberry Pi Pico W:

* **Introduction**: introduces the tutorial and acknowledges the sponsor, SunFounder. He explains the goal of adding a toggle push button to the existing temperature and humidity measurement setup.

* **Previous Lessons Recap**: Reviews the previous lesson on using the DHT11 sensor and sets the context for the current task.

**Component Introduction and Circuit Setup**:
- Reintroduces the DHT11 sensor and explains the addition of a push button to the circuit.
- Describes the connections:
  - DHT11 sensor:
    - Pin 1 to 3.3V
    - Pin 2 to GPIO pin 16
    - Pin 4 to ground
  - Push button:
    - One leg to ground
    - The other leg to GPIO pin 15
* **Code Explanation**:
 - Imports necessary libraries: machine, utime (as time), and DHT.
 - Sets up GPIO pins for the DHT11 sensor and the push button.
 - Creates a toggle mechanism to switch between temperature units (Celsius and Fahrenheit).
 - Reads the button state and toggles the temperature unit when the button is pressed and released.
 - Measures and converts temperature from Celsius to Fahrenheit.
 - Prints temperature and humidity readings in a single line using `\r` for a clean output.
 - Addresses formatting issues to ensure the output displays correctly when toggling between Celsius and Fahrenheit.
* **Practical Demonstration**:
 - Runs the code to observe temperature and humidity readings.
 - Demonstrates the toggle functionality between Celsius and Fahrenheit when the button is pressed.
 - Fixes formatting issues to ensure the output is clean and consistent.
* **Homework Assignment**:
 - Adds more toggle functionality to the project.
 - Implements additional toggles to switch between displaying temperature in Celsius, Fahrenheit, and humidity one at a time.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/MrfIfndX7OM?si=d1WrCY-6Ui7J2DWb" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

