.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 36 : Control a Servo With MicroPython
=============================================================================
This tutorial covers controlling a servo motor using the Raspberry Pi Pico W:

* **Servo Motor Control**: 
 - Introduction to using the SG90 servo motor with the Raspberry Pi Pico W.
 - Explanation of servo motor connections: brown (ground), red (power), orange (control).
 - Emphasis on not using the Raspberry Pi Pico W to power larger servos due to potential damage.
* **Wiring Diagram and Setup**:
 - Detailed wiring instructions for connecting the SG90 servo to the Raspberry Pi Pico W.
 - Use of GPIO pin 15 for control, and creating a power rail from pin 1 for 5V supply.
* **PWM Basics**:
 - Explanation of Pulse Width Modulation (PWM) and its role in controlling servo position.
 - Calculation of pulse widths corresponding to different servo angles (0.5ms for 0 degrees, 2.5ms for 180 degrees).
 - Setting PWM frequency to 50Hz to match the servo's requirements.
* **Code Explanation**:
 - Step-by-step coding tutorial to set up PWM on GPIO pin 15.
 - Creating a function to convert desired angles to PWM duty cycle values.
 - Example code to control the servo by entering desired angles.
* **Practical Demonstration**:
 - Running the code to move the servo to specific angles.
 - Ensuring safe servo operation by avoiding manual rotation of the servo horn.
* **Homework Assignment**:
 - Task to integrate a potentiometer with the setup to control the servo position by adjusting the potentiometer.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/vAnd0AC6u1Q?si=0VAnHzQFnQlyDqI6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
