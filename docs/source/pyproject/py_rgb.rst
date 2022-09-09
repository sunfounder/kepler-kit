.. _py_rgb:


2.4 Colorful Light
==============================================

As we know, light can be superimposed. For example, mix blue light and green light give cyan light, red light and green light give yellow light.
This is called "The additive method of color mixing".

* `Additive color - Wikipedia <https://en.wikipedia.org/wiki/Additive_color>`_

Based on this method, we can use the three primary colors to mix the visible light of any color according to different specific gravity. For example, orange can be produced by more red and less green.

In this chapter, we will use RGB LED to explore the mystery of additive color mixing!

RGB LED is equivalent to encapsulating Red LED, Green LED, Blue LED under one lamp cap, and the three LEDs share one cathode pin.
Since the electric signal is provided for each anode pin, the light of the corresponding color can be displayed. By changing the electrical signal intensity of each anode, it can be made to produce various colors.

* :ref:`cpn_rgb`

**Schematic**

|sch_rgb|

The PWM pins GP13, GP14 and GP15 control the Red, Green and Blue pins of the RGB LED respectively, and connect the common cathode pin to GND. This allows the RGB LED to display a specific color by superimposing light on these pins with different PWM values.




**Wiring**

|img_rgb_pin|

The RGB LED has 4 pins: the long pin is the common cathode pin, which is usually connected to GND; the left pin next to the longest pin is Red; and the two pins on the right are Green and Blue.


|wiring_rgb|


**Code**



.. note::

    * Open the ``2.4_colorful_light.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    red = machine.PWM(machine.Pin(13))
    green = machine.PWM(machine.Pin(14))
    blue = machine.PWM(machine.Pin(15))
    red.freq(1000)
    green.freq(1000)
    blue.freq(1000)

    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def color_to_duty(rgb_value):
        rgb_value = int(interval_mapping(rgb_value,0,255,0,65535))
        return rgb_value

    def color_set(red_value,green_value,blue_value):
        red.duty_u16(color_to_duty(red_value))
        green.duty_u16(color_to_duty(green_value))
        blue.duty_u16(color_to_duty(blue_value))

    color_set(255,128,0)

Here, we can choose our favorite color in drawing software (such as paint) and display it with RGB LED.

|img_take_color|

Write the RGB value into ``color_set()``, you will be able to see the RGB light up the colors you want.


**How it works?**

To allow the three primary colors to work together, we defined a ``color_set()`` function.

At present, pixels in computer hardware usually use 24-bit representations. Each primary color is divided into 8 bits, and the color value range is 0 to 255. There are 256 possible combinations of each of the three primary colors (don't forget to count 0! ), so 256 x 256 x 256 = 16,777,216 colors.
The ``color_set()`` function also uses 24-bit notation, so we can choose a color more easily.

And since the value range of ``duty_u16()`` is 0~65535 (instead of 0 to 255) when the output signals to RGB LED through PWM, we have defined ``color_to_duty()`` and ``interval_mapping ()`` function to map the color values to the duty values.