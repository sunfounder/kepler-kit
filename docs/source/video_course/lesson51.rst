.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

Lesson 51: Ultimate Pitch and Roll Gadget Using the MPU6050
=============================================================================
This tutorial covers creating a precise tilt meter using the MPU6050 sensor and Raspberry Pi Pico W:

* **Setup**: Connect the MPU6050 and OLED 1306 to the Raspberry Pi Pico W.
* **Challenges**: Accelerometer data is noisy, and gyroscope data drifts over time.
* **Solution**: Use a complementary filter to combine accelerometer and gyroscope data, with error correction for steady state errors.
* **Implementation**: Initialize sensors and OLED. Collect and filter data, displaying tilt as both a bubble level and degree readout on the OLED.
* **Demonstration**: Test for stable pitch and roll readings, with portable battery-powered operation.
* **Additional Improvements**: Consider wireless monitoring or creating a 3D-printed case for portability.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/afQyZl2hkd0?si=4Dg4Uvr5yVC4f60Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
