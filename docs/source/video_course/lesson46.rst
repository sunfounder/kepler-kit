.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

Lesson 46: Build a 2 Axis Tilt Meter with Display Using the MPU6050
=============================================================================
This tutorial covers using the MPU6050 sensor with the Raspberry Pi Pico W to create a two-axis tilt meter:

* **Setup**: Connect MPU6050 and OLED 1306 to Raspberry Pi Pico W.
* **Concept**: Measure tilt using pitch and roll angles, display bubble level on OLED.
* **Equation**: 
   - Pitch: \(\arctan\left(\frac{Y}{Z}\right)\)
   - Roll: \(\arctan\left(\frac{X}{Z}\right)\)
   - Convert radians to degrees.
* **Code**: Set up libraries, measure X, Y, Z acceleration, calculate angles, and display on OLED.
* **Demonstration**: Test tilt, adjust bubble movement for responsiveness.
* **Advanced**: Stabilize tilt readings to avoid errors from acceleration or vibrations.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/wYv39RMwXvU?si=6gJoFFIa1HSdGIFt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
