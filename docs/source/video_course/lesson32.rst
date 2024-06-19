.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 32: Mobile Weather Station Project
=============================================================================

This tutorial covers creating a portable weather station using the Raspberry Pi Pico W:

* **Connecting to WiFi**:
 - Import necessary libraries.
 - Create a WLAN object and connect to the WiFi network.
* **Fetching Weather Data**:
 - Use the OpenWeatherMap API to fetch real-time weather data.
 - Obtain an API key from OpenWeatherMap by signing up for a free account.
* **Parsing JSON Data**:
 - Extract relevant weather information such as temperature, humidity, barometric pressure, sunrise, and sunset times.
* **Displaying Data on OLED**:
 - Set up an OLED display and connect it to the Raspberry Pi Pico W.
 - Use the `ssd1306` library to display weather data on the OLED screen.
 - Create a loop to periodically update the weather data on the screen.
* **Powering the Device**:
 - Connect the Raspberry Pi Pico W to a battery for portable use.
* **Code Explanation**:
 - Step through initializing the OLED display and connecting to WiFi.
 - Fetch and parse weather data, then display it on the OLED screen.
 - Implement a loop to update the weather data every few minutes.
* **Homework Assignment**:
 - Enhance the project by adding an RGB LED to visually indicate weather conditions such as temperature, humidity, or wind speed.



**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/zovC4CvR1Hw?si=d_lhJvfzTC3pR5cS" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
