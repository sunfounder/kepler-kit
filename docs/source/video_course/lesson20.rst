.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 20:  Using the DHT11 Temperature and Humidity Sensor in MicroPython
=============================================================================

This tutorial covers measuring temperature and humidity using the DHT11 sensor with the Raspberry Pi Pico W:

* **Introduction**: introduce the lesson, focuse on using the DHT11 sensor to measure temperature and humidity.
* **Previous Lessons Recap**: Recaps the foundational skills learned in previous lessons, such as digital writes, analog writes using PWM, digital reads, and analog reads.
* **Component Introduction**: Introduces the DHT11 sensor from the SunFounder Kepler kit and demonstrates how to find it within the kit.
* **Circuit Setup**:
 - Establishes ground and power rails on the breadboard.
 - Connects the DHT11 sensor to the Raspberry Pi Pico W:
   - Pin 1 of the sensor to 3.3V.
   - Pin 2 of the sensor to GPIO pin 16 (physical pin 21).
   - Pin 4 of the sensor to ground.
* **Code Explanation**:
 - Imports necessary libraries: machine, utime (as time), and DHT.
 - Sets up the GPIO pin for data input with a pull-down resistor.
 - Initializes the DHT11 sensor.
 - Enters an infinite loop to continuously measure and print temperature and humidity.
 - Explains how to format the printed output to display temperature and humidity in a single line using `\r`.
* **Practical Demonstration**:
 - Runs the code and observes temperature and humidity readings in real-time.
 - Discusses the importance of not using methods that might cause condensation on the sensor to test changes in readings.
* **Formatting Output**:
 - Demonstrates how to format the output to show the temperature in degrees Celsius and humidity in percentage.
 - Explains how to print the degree symbol using ASCII character codes.
* **Homework Assignment**:
 - Adds a push button to the circuit.
 - Modifies the code to toggle between displaying temperature in Celsius and Fahrenheit when the button is pressed.



**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/KYEidJFYPto?si=5vAk5sl-VyEqYIfs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

