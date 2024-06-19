.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

lesson 30: Project to Connect Your Raspberry Pi Pico W to the Internet
=============================================================================

This tutorial covers connecting the Raspberry Pi Pico W to the internet and fetching data from APIs:

**Introduction**:
- The goal is to connect the Raspberry Pi Pico W to the internet and fetch real-time data from APIs.
- No additional hardware setup required.
**Connecting to WiFi**:
- Import necessary libraries: `network`, `time`, `urequests`.
- Create a WLAN object and connect to the WiFi network.
- Ensure successful connection before proceeding.
**Fetching Data from APIs**:
- Introduction to JSON files and their structure (arrays, dictionaries, nested elements).
- Example API used: Fetching real-time data about astronauts in space.
- Parse and print the data structure to understand its format.
**Code Explanation**:
- Use `urequests.get()` to fetch JSON data from a specified API endpoint.
- Parse the JSON data to extract relevant information.
- Example: List names of astronauts currently in space and their respective spacecraft.
**Practical Demonstration**:
- Code snippet to fetch and display data about astronauts.
- Demonstrates how to navigate nested JSON structures to extract specific data.
- Example output: Number of astronauts, their names, and spacecraft.
**Homework Assignment**:
- Find an interesting real-time data set (e.g., weather, stock prices, earthquakes).
- Fetch and parse the data using the Raspberry Pi Pico W.
- Display or utilize the data in a meaningful way (e.g., sensorless weather station).


**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/5xXHo1xhc-g?si=kdpYgB6P7KoUU2Xa" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
