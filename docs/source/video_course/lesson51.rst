.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 51 : Ultimate Pitch and Roll Gadget Using the MPU6050
=============================================================================
This tutorial covers creating a precise tilt meter using the MPU6050 sensor and Raspberry Pi Pico W:

* **Setup**:
   - Connect the MPU6050 and OLED 1306 to the Raspberry Pi Pico W using the provided schematic.
* **Challenges**:
   - Raw accelerometer data is noisy.
   - Gyroscope data drifts over time.
* **Solution**:
   - Combine accelerometer and gyroscope data using a complementary filter to achieve accurate, fast, and low-noise tilt measurements.
   - Implement error correction to handle steady state errors.
* **Implementation**:
   - Initialize the MPU6050 and OLED 1306.
   - Collect data from both accelerometer and gyroscope.
   - Apply a complementary filter to combine short-term gyroscope data with long-term accelerometer data.
   - Add error correction to compensate for any drift in the measurements.
   - Display the results on the OLED screen, showing both qualitative (bubble level) and quantitative (degree readout) tilt information.
* **Demonstration**:
   - The tilt meter is tested to show stable and accurate pitch and roll readings even with vibrations.
   - The device is made portable using a battery pack, enabling it to operate untethered.
* **Additional Improvements**:
   - Suggestions include making the device wireless for remote monitoring or designing a 3D printed case for portability.



**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/afQyZl2hkd0?si=4Dg4Uvr5yVC4f60Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
