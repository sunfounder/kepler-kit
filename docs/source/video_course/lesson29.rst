.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 29: Simple Client Server Project to Control RGB LED
=============================================================================

This tutorial covers setting up a remote-controlled RGB LED using a Raspberry Pi Pico W and a PC over Wi-Fi:

* **Introduction**: Goal is to control an RGB LED on a Raspberry Pi Pico W remotely using Wi-Fi.
* **Wiring Diagram and Setup**: Connect RGB LED to GPIO pins 16, 17, 18, and OLED to GPIO pins 2 (SDA) and 3 (SCL).
* **Server Side Setup**: Import libraries, initialize GPIO pins, connect to Wi-Fi, create a UDP server, and display the IP on the OLED.
* **Client Side Setup**: Create a UDP client on the PC to send color commands to the server.
* **Practical Demonstration**: Show changing RGB LED color via commands sent from the PC, with the OLED displaying the commands and IP.
* **Final Setup and Testing**: Power the Raspberry Pi Pico W with a battery, save the code as ``main.py``, and demonstrate wireless operation.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/eZTETVkX-N8?si=TtZ6B4-Ljm75rhPB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
