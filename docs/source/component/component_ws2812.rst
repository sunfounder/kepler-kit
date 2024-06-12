.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _cpn_ws2812:

WS2812 RGB 8 LEDs Strip
============================

|img_ws2812|

The WS2812 RGB 8 LEDs Strip is composed of 8 RGB LEDs. 
Only one pin is required to control all the LEDs. Each RGB LED has a WS2812 chip, which can be controlled independently. 
It can realize 256-level brightness display and complete true color display of 16,777,216 colors. 
At the same time, the pixel contains an intelligent digital interface data latch signal shaping amplifier drive circuit, 
and a signal shaping circuit is built in to effectively ensure the color height of the pixel point light Consistent.

It is flexible, can be docked, bent, and cut at will, and the back is equipped with adhesive tape, which can be fixed on the uneven surface at will, and can be installed in a narrow space.

**Features**

* Work Voltage: DC5V
* IC: One IC drives one RGB LED
* Consumption: 0.3w each LED
* Working Temperature: -15-50
* Color: Full color RGB
* RGB Type: 5050RGB(Built-in IC WS2812B)
* Light Strip Thickness: 2mm
* Each LED can be controlled individually

**WS2812B Introdction**

* `WS2812B Datasheet <https://cdn-shop.adafruit.com/datasheets/WS2812B.pdf>`_

WS2812B is a intelligent control LED light source that the control circuit and RGB chip are integrated in
a package of 5050 components. It internal include intelligent digital port data latch and signal reshaping amplification drive circuit. Also include a precision internal oscillator and a 12V voltage programmable constant current control part, effectively ensuring the pixel point light color height consistent.

The data transfer protocol use single NZR communication mode. After the pixel power-on reset, the DIN
port receive data from controller, the first pixel collect initial 24bit data then sent to the internal data latch,
the other data which reshaping by the internal signal reshaping amplification circuit sent to the next cascade
pixel through the DO port. After transmission for each pixel, the signal to reduce 24bit. pixel adopt auto resha
-ping transmit technology, making the pixel cascade number is not limited the signal transmission, only depend
on the speed of signal transmission.

LED with low driving voltage, environmental protection and energy saving, high brightness, scattering angle is large, good consistency, low power, long life and other advantages. The control chip integrated in LED
above becoming more simple circuit, small volume, convenient installation.

.. Example
.. -------------------

.. :ref:`RGB LED Strip`


**Example**

* :ref:`py_neopixel` (For MicroPython User)
* :ref:`py_music_player` (For MicroPython User)
* :ref:`ar_neopixel` (For Arduino User)
* :ref:`per_flowing_leds` (For Piper Make User)
