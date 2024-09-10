.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 59 : Controlling a Servo with a Joystick
=============================================================================

This tutorial covers controlling a servo with a joystick using the Raspberry Pi Pico W:


* **Wiring Setup**: Connect joystick ground to pin 38, 3.3V to pin 36, VRX to GPIO 27, VRY to GPIO 26. Connect servo 5V to pin 40, ground to pin 38, control to GPIO 15.
* **Code Implementation**: Import ``machine``, ``time``, ``math``. Set up ADC for joystick and PWM for servo. Read and print joystick values.
* **Calibration and Control**: Scale ADC values to -100 to +100. Calculate joystick angle. Map angle to PWM for servo.
* **Homework Assignment**: Write code to control servo from joystick angle (0-180 degrees).


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/ayY2wOJmrUE?si=HKP8qwd4WMC1et2r" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
