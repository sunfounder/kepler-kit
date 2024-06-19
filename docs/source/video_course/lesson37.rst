.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 37 : Control a Servo With a Potentiometer in MicroPython
=============================================================================
This tutorial covers controlling a servo motor using a potentiometer with the Raspberry Pi Pico W:

* **Servo Motor Control**:
 - Connect the SG90 servo motor to the Raspberry Pi Pico W.
 - Brown wire to ground, red wire to power (5V), orange wire to GPIO pin 15 for control.
* **Wiring Setup**:
 - Connect the potentiometer: power to 3.3V, ground to ground rail, and signal to GPIO pin 26.
* **PWM Basics**:
 - Use Pulse Width Modulation (PWM) to control servo position.
 - Set PWM frequency to 50Hz for the servo.
* **Code Explanation**:
 - Set up PWM on GPIO pin 15.
 - Convert potentiometer readings to servo angles.
 - Example code provided to move the servo based on potentiometer input.
* **Practical Demonstration**:
 - Run the code to control the servo with the potentiometer.
 - Avoid manually rotating the servo horn to prevent damage.
* **Application Ideas**:
 - Control larger servos with an external power supply for more advanced projects.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/iiJasGsLTrQ?si=f-avwQIJNypRuh4t" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
