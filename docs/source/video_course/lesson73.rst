.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 73 :  Control a RGB LED Using a Dictionary in MicroPython
===================================================================================

This tutorial covers controlling an RGB LED with the Raspberry Pi Pico W using dictionaries:

* **Wiring Setup**:
- Connect the RGB LED to the Raspberry Pi Pico W:
  - R leg to GPIO pin 14 through a 330 Ohm resistor.
  - G leg to GPIO pin 13.
  - B leg to GPIO pin 12 through a 330 Ohm resistor.
  - Ground leg to the ground rail.
* **Code Implementation**:
- **Create Dictionary**:
   - Define a dictionary with color names as keys and their respective RGB values as lists.
- **Import Libraries**:
   - Import necessary libraries (`machine`, `time`).
   - Set up PWM for the RGB LED pins.
- **Main Program Loop**:
   - Continuously prompt the user to input a desired color.
   - Convert input to lowercase and check if it's a valid color.
   - If valid, adjust the LED colors using PWM duty cycles based on the dictionary values.
   - Implement error handling for invalid inputs.
- **Function to Set Color**:
   - Define a function `make_color` that takes the desired color and sets the RGB LED accordingly using PWM.
   
* **Homework Assignment**:
   - Extend the program by moving the `make_color` function into a library and importing it into the main program.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/1CHcjlaBvGY?si=feXCiEMKRkdsLx4y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
