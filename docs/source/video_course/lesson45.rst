.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

Lesson 45: Calculating Height from a Dropped Object in Freefall
=============================================================================
This tutorial covers using the MPU6050 sensor with the Raspberry Pi Pico W to measure vertical distances:

* **Setup**: Connect the MPU6050 and OLED 1306 to the Raspberry Pi Pico W, ensuring secure connections to reduce noise.
* **Concept**: Measure vertical distance by calculating the time (T_drop) in freefall and use it to determine the height dropped.
* **Equation**: Calculate height (H) with \( H = 16 \times (T_{drop})^2 \), converting time from milliseconds to seconds.
* **Code Implementation**: Set up libraries, measure Z-axis acceleration to detect 0G, start a timer during freefall, and display height and drop time on the OLED.
* **Practical Demonstration**: Test by dropping the sensor from known heights and adjust for accuracy as needed.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/xpHDAcdrTF0?si=NdmV4J5G6DhJ4f6M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
