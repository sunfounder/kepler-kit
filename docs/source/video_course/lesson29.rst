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

* **Introduction**:
 - The goal is to control an RGB LED on a Raspberry Pi Pico W remotely from a PC using Wi-Fi.
* **Wiring Diagram and Setup**:
 - RGB LED's red, green, and blue channels are connected to GPIO pins 16, 17, and 18, respectively.
 - OLED display is connected via I2C to GPIO pins 2 (SDA) and 3 (SCL).
* **Server Side Setup (Raspberry Pi Pico W)**:
 - Import libraries: `socket`, `time`, `network`, `machine`, `ssd1306`.
 - Initialize GPIO pins for the RGB LED and OLED display.
 - Connect to Wi-Fi and obtain an IP address.
 - Create a UDP server socket and bind it to the IP address and a port.
 - Display the IP address and port on the OLED screen.
 - Listen for incoming commands, decode them, and display the command and sender's address.
* **Client Side Setup (PC)**:
 - Import the `socket` library.
 - Define the server address and port.
 - Create a UDP client socket.
 - Get user input for the LED color, encode the command, and send it to the server.
 - Wait for and print the server's response.
* **Practical Demonstration**:
 - Demonstrate sending commands from the client to change the RGB LED color on the server.
 - OLED display shows the received commands and the sender's IP address.
* **Final Setup and Testing**:
 - Disconnect the Raspberry Pi Pico W from USB and power it with a battery.
 - Save the code as `main.py` to run on startup.
 - Demonstrate fully wireless operation by sending commands from the PC and observing the RGB LED changes and OLED updates.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/eZTETVkX-N8?si=TtZ6B4-Ljm75rhPB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
