.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 35 : Remote Weather Station with RGB LED Temperature Indicator
=============================================================================
This tutorial covers integrating an RGB LED to display temperature data on a weather station using the Raspberry Pi Pico W:

* **Project Overview**:
 - Build a remote weather station using Raspberry Pi Pico W, an OLED display, and an RGB LED to show temperature visually.
* **HSV to RGB Conversion**:
 - Convert temperature values to colors using the HSV color wheel.
 - Map temperatures from -20°F (deep violet) to 120°F (red) to corresponding angles on the color wheel.
* **Circuit Setup**:
 - Connect the OLED display and RGB LED to the Raspberry Pi Pico W.
 - Configure GPIO pins and PWM for the RGB LED.
* **Coding**:
 - Fetch temperature data, calculate the hue angle, convert it to RGB values, and apply these to the RGB LED.
 - Integrate the HSV to RGB conversion library into the weather station code.
* **Demonstration**:
 - Display temperature data on the OLED and RGB LED.
 - Save and run the code, making the setup portable with battery power.
* **Conclusion**:
 - Customize the project by adjusting color mappings and temperature ranges.
 - Encouragement to subscribe, comment, and share the tutorial.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/c9tQHyQWIYk?si=ORHsIXt8eBGeXDdp" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
