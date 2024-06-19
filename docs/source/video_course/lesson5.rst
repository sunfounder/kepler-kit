.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 5:  Reading Analog Voltages Using a Potentiometer
=================================================================

This tutorial covers reading analog voltages using the SunFounder Kepler Kit for Raspberry Pi Pico W:
* **Analog Voltage Reading**: Explains the importance of reading analog voltages for various sensor inputs and user inputs, like potentiometers, to control aspects such as volume or brightness.
* **Wiring Diagram and Setup**: Provides a detailed explanation of the potentiometer's workings and how to connect it to the Pico W. Describes setting up ground and 3.3V rails and connecting the potentiometer's middle pin to GPIO pin 28.
* **Code Explanation**: Describes writing Python code to read analog voltages. Covers importing necessary libraries, setting up GPIO pins, creating an object for the potentiometer, and using a while loop to continuously read and print voltage values.
* **Mathematical Conversion**: Teaches how to convert the raw ADC values (0 to 65535) to actual voltage values (0 to 3.3V) using linear equations. Demonstrates the process of deriving the equation of the line from two known points and applying it in the code.
* **Practical Demonstration**: Shows the code in action, reading and converting the potentiometer values to voltage and displaying them. Discusses the accuracy and expected results when adjusting the potentiometer.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/ODWwErH_iGA?si=EzLxy17TO462G6_r" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

