.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 26:  Drawing a Circle on the OLED 1306 Display
=============================================================================

This tutorial covers drawing shapes on an OLED display using the Raspberry Pi Pico W:

* **Introduction**:
 - Highlights the goal: drawing a circle on an OLED display using the Raspberry Pi Pico W.
* **Recap and Setup**:
 - Reviews the previous lesson on using the OLED 1306 display and setting up the SSD1306 library.
 - Discusses the importance of using mathematical functions to draw shapes on the OLED display.
* **Drawing a Circle**:
 - Explains the math behind drawing a circle using trigonometric functions: \( x = r \cos(\theta) \) and \( y = r \sin(\theta) \).
 - Converts degrees to radians for use in programming languages.
 - Shows how to center the circle on the OLED display by adjusting the x and y coordinates.
 - Provides a step-by-step code example to draw a circle by iterating through 360 degrees and calculating the x and y positions.
* **Enhancing the Circle Drawing**:
 - Demonstrates how to draw a filled circle by iterating over a range of radii.
 - Shows how to draw a partial circle or arc by adjusting the angle range.
* **Practical Demonstration**:
 - Runs the code to show the drawing of a circle and a filled circle on the OLED display.
 - Explains how to optimize the drawing speed by updating the display only after all points are calculated.
* **Homework Assignment**:
 - Assigns a task: create a program that draws a "floating potato chip" shape on the OLED display.
 - Encourages viewers to figure out the math behind the shape and post their homework on YouTube.




**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/VgCcBm_Ms3E?si=J175coTlAdw2EMZ_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
