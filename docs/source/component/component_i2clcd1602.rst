.. _cpn_lcd:

I2C LCD1602 Module
================================

A liquid crystal display (LCD) is a flat panel display or other electronically modulated optical device using light modulation characteristics of liquid crystals with a combined polarizer. Liquid crystals do not emit light directly, but use a backlight or reflector to produce color or monochrome images.

LCDs are used in a wide range of applications, including LCD televisions, computer monitors, instrument panels, aircraft cockpit displays, and indoor and outdoor signage. Small LCDs are common in portable consumer devices, such as digital cameras, watches, digital clocks, calculators and cell phones, including smartphones. LCD screens are also used in consumer electronics, such as DVD players, video game devices and clocks.


LCD1602 is a character type liquid crystal display, which can display 32 (16*2) characters at the same time.

|img_i2c_lcd|

* `Liquid Crystal Display - Wikipedia <https://en.wikipedia.org/wiki/Liquid-crystal_display>`_


**I2C communication**

As we all know, though LCD and some other displays greatly enrich the man-machine interaction, they share a common weakness. When they are connected to a controller, multiple IOs will be occupied of the controller which has no so many outer ports. Also it restricts other functions of the controller. Therefore, LCD1602 with an I2C bus is developed to solve the problem.


I2C(Inter-Integrated Circuit) bus is a very popular and powerful bus for communication between a master device (or master devices) and a single or multiple slave devices.
I2C main controller can be used to control IO expander, various sensors, EEPROM, ADC/DAC and so on. All of these are controlled only by the two pins of host, the serial data (SDA1) line and the serial clock line(SCL1). 

* `Inter-Integrated Circuit - Wikipedia <https://en.wikipedia.org/wiki/I2C>`_

.. Example
.. -------------------

.. :ref:`liquid_crystal_display`


**Example**

* :ref:`py_lcd` (For MicroPython User)
* :ref:`py_room_temp` (For MicroPython User)
* :ref:`py_guess_number` (For MicroPython User)
* :ref:`ar_lcd` (For Arduino User)