.. _cpn_rgb:

RGB LED
=================

|img_rgb|
    
RGB LEDs emit light in various colors. An RGB LED packages three LEDs of red, green, and blue into a transparent or semitransparent plastic shell. It can display various colors by changing the input voltage of the three pins and superimpose them, which, according to statistics, can create 16,777,216 different colors. 

|img_rgb_light|

RGB LEDs can be categorized into common anode and common cathode ones. In this kit, the latter is used. The **common cathode**, or CC, means to connect the cathodes of the three LEDs. After you connect it with GND and plug in the three pins, the LED will flash the corresponding color. 

Its circuit symbol is shown as figure.

|img_rgb_symbol| 

An RGB LED has 4 pins: the longest pin is the common cathode pin, which is usually connected to GND, the left pin next to the longest pin is Red, and the 2 pins on the right are Green and Blue.

|img_rgb_pin|


* `RGB systems - Wikipedia <https://en.wikipedia.org/wiki/Light-emitting_diode#RGB_systems>`_

.. Example
.. -------------------

.. :ref:`Colorful Light`


**Example**

* :ref:`py_rgb` (For MicroPython User)
* :ref:`py_fruit_piano` (For MicroPython User)
* :ref:`ar_rgb` (For Arduino User)
* :ref:`per_rainbow_light` (For Piper Make User)