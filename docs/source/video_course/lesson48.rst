.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 48 : Measuring Rotation Using the Gyros on the MPU6050
=============================================================================

This tutorial covers using the MPU6050 sensor with the Raspberry Pi Pico W to create a stable tilt meter by combining accelerometer and gyroscope data:

* **Setup**:
   - Connect the MPU6050 to the Raspberry Pi Pico W using the provided schematic.
* **Concept**:
   - Measure tilt using both accelerometer and gyroscope data.
   - Address errors from acceleration noise and gyroscope drift.
* **Low-Pass Filter**:
   - Smooth accelerometer data to reduce noise.
* **Gyroscope Integration**:
   - Calculate tilt angles using rotational velocity.
   - Update pitch, roll, and yaw angles continuously.
* **Combining Data**:
   - Fuse accelerometer and gyroscope data to minimize noise and drift.
* **Homework**:
   - Implement and fine-tune the described method for stable tilt measurement.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/XZIJasvCB44?si=hx0Ulyd0pTnro8sd" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
