.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 16:  Sequence of Colors in RGB LED With Micropython
=============================================================================

This tutorial covers using for loops in MicroPython with the Raspberry Pi Pico W to control an RGB LED:

* **Introduction**: The lesson starts with a brief introduction and an overview of the lesson, focusing on using for loops and PWM (Pulse Width Modulation) to control the brightness and color of an RGB LED.
* **Circuit Setup**: Demonstrates the wiring of the RGB LED to the Raspberry Pi Pico W, using GPIO pins 13, 14, and 15 for the red, green, and blue channels, respectively. Emphasizes the importance of using 330 Ohm current limiting resistors.
* **PWM Setup**: Explains setting up PWM channels for each LED color, establishing a frequency of 1000 Hz to ensure smooth transitions without visible flickering.
* **Color Sequence Input**: Shows how to prompt the user for a sequence of colors and capture the input. Uses a for loop to store the user-defined colors in an array, ensuring that the input is converted to lowercase for consistency.
* **Color Control Logic**: Details the logic for setting the brightness of each LED color based on the user's input. Implements if statements to assign PWM values to create different colors, including red, green, blue, cyan, magenta, yellow, orange, and off.
* **Continuous Loop for Displaying Colors**: Uses a while true loop to continuously cycle through the user-defined color sequence. Adds sleep statements to control the duration each color is displayed.
* **Practical Demonstration**: Provides a step-by-step demonstration of running the code, entering a sequence of colors, and observing the RGB LED displaying the colors in the specified order.
* **Next Steps**: Announces that the next lesson will cover using push buttons with the Raspberry Pi Pico W to read digital inputs, completing the learning of input and output methods before moving on to more advanced components.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/VivNlgYg3wY?si=ECUsRAWanIAShyxk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

