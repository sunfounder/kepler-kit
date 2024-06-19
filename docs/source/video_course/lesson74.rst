.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 74 :  Create a MicroPython Class for Controlling RGB LED
===================================================================================

This tutorial covers creating a MicroPython library for controlling an RGB LED with the Raspberry Pi Pico W:

* **Wiring Setup**: 
  - Connect the RGB LED to the Raspberry Pi Pico W:
  - R leg to GPIO pin 14 through a 330 Ohm resistor.
  - G leg to GPIO pin 13.
  - B leg to GPIO pin 12 through a 330 Ohm resistor.
  - Ground leg to the ground rail.

* **Code Implementation**: 
* **Create Library**:Define a class `RGB_LED` in a MicroPython library to handle the RGB LED.Include a dictionary for color values within the class.Create methods for initializing the LED pins and setting the colors using PWM.
* **Import Libraries**:Import necessary libraries (`machine`, `time`).Set up PWM for the RGB LED pins within the class methods.
* **Main Program**:Import the custom library and create an object for the RGB LED.Use a while loop to continuously prompt the user to input a desired color.Validate the input and set the LED color accordingly.Implement error handling for invalid inputs and clean exit functionality using a keyboard interrupt.
* **Homework Assignment**:Extend the program by adding more features to the MicroPython library, such as additional color settings or patterns, and ensure that the main program remains simple and easy to read by utilizing the library effectively.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/tw-mXURNEUc?si=Ja75F1-I6MYwJgEh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
