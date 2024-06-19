.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 31: Sensorless Remote Weather Station Project
=============================================================================

This tutorial covers creating a sensorless weather station using the Raspberry Pi Pico W:

* **Connecting to WiFi**:
 - Import necessary libraries.
 - Create a WLAN object and connect to the WiFi network.
* **Fetching Weather Data**:
 - Use the OpenWeatherMap API to fetch real-time weather data.
 - Obtain an API key from OpenWeatherMap by signing up for a free account.
* **Parsing JSON Data**:
 - Extract relevant weather information such as temperature, humidity, barometric pressure, sunrise, and sunset times.
* **Code Explanation**:
 - Use `urequests.get()` to fetch JSON data from the API endpoint.
 - Convert Unix epoch time to local time for sunrise and sunset.
 - Convert barometric pressure from HPA to atmospheres.
* **Displaying Weather Data**:
 - Print weather information like temperature, humidity, barometric pressure, conditions, and wind speed.
* **Homework Assignment**:
 - Enhance the project by adding a display to show the weather information.
 - Create a portable, battery-powered weather station.


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/hbcA90S7Jtk?si=mHMxKUEEpqiYM7DA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
