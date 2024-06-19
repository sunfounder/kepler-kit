.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 46 : Build a 2 Axis Tilt Meter with Display Using the MPU6050
=============================================================================
This tutorial covers using the MPU6050 sensor with the Raspberry Pi Pico W to create a two-axis tilt meter:

* **Setup**:
   - Connect the MPU6050 and OLED 1306 to the Raspberry Pi Pico W using the provided schematic. Ensure all connections are secure to avoid electrical noise.
* **Concept**:
   - Measure the tilt of the sensor using the MPU6050's accelerometer data to calculate pitch and roll angles. Use these angles to create a visual representation of a bubble level on the OLED display.
* **Equation**:
   - Calculate pitch and roll angles using the following formulas:
     - Pitch: \(\text{Pitch} = \arctan\left(\frac{\text{Y acceleration}}{\text{Z acceleration}}\right)\)
     - Roll: \(\text{Roll} = \arctan\left(\frac{\text{X acceleration}}{\text{Z acceleration}}\right)\)
   - Convert these angles from radians to degrees.
* **Code Implementation**:
   - Set up the MPU6050 and OLED 1306 libraries.
   - Measure the X, Y, and Z acceleration values.
   - Calculate pitch and roll angles in degrees.
   - Display the calculated pitch and roll angles on the OLED along with a visual representation of a bubble moving within a rectangle to indicate tilt.
* **Practical Demonstration**:
   - Test the setup by tilting the sensor and observing the bubble's movement on the OLED display. Adjust the sensitivity of the bubble's movement to make the tilt meter more responsive.
   - Ensure the readings are accurate and the bubble moves smoothly according to the tilt angles.
* **Advanced Considerations**:
   - Address the challenge of the accelerometer interpreting acceleration and deceleration as tilt. Think about strategies to stabilize the readings and prevent incorrect tilt detection due to vibrations or movements.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/wYv39RMwXvU?si=6gJoFFIa1HSdGIFt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
