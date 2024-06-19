.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 45 : Calculating Height from a Dropped Object in Freefall
=============================================================================
This tutorial covers using the MPU6050 sensor with the Raspberry Pi Pico W to measure vertical distances:

* **Setup**:
   - Connect the MPU6050 and OLED 1306 to the Raspberry Pi Pico W using the provided schematic. Ensure all connections are secure to avoid electrical noise.
* **Concept**:
   - Measure vertical distances by dropping the sensor and calculating the time it takes to fall (T_drop). Use the time in freefall to calculate the height dropped.
* **Equation**:
   - The height (H) is calculated using the formula: \( H = 16 \times (T_{drop})^2 \). Convert the drop time from milliseconds to seconds before applying the formula.
* **Code Implementation**:
   - Set up the MPU6050 and OLED 1306 libraries.
   - Measure the Z-axis acceleration to detect when the sensor is in freefall (measuring 0G).
   - Start a timer when the sensor is dropped and stop it when it hits the ground.
   - Display the calculated height and drop time on the OLED.
* **Practical Demonstration**:
   - Test the setup by dropping the sensor from known heights and verifying the accuracy of the measurements. Adjust as needed to improve precision.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/xpHDAcdrTF0?si=NdmV4J5G6DhJ4f6M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
