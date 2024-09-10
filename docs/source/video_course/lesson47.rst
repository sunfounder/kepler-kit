.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 47 : Improving Sensor Data With a Low Pass Filter
=============================================================================
This tutorial covers using the MPU6050 sensor with the Raspberry Pi Pico W to create a stable two-axis tilt meter by implementing a low-pass filter:

* **Setup**: Connect the MPU6050 to the Raspberry Pi Pico W.
* **Concept**: Measure tilt using accelerometer data, addressing errors from acceleration.
* **Low-Pass Filter**: Implement to smooth data using the equation: ``\(\text{new value} = \text{confidence} \times \text{measurement} + (1 - \text{confidence}) \times \text{old value}\)``.
* **Code**: Measure X, Y, Z, filter pitch and roll angles, and display results.
* **Homework**: Test the low-pass filter and experiment with confidence values.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/3YqGIg4crEk?si=rwiDFcJ98nlj_Sg3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
