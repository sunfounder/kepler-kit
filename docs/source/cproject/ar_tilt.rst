.. _ar_tilt:

2.6 - Tilt It！
==========================

|img_tilt|

The tilt switch is a 2-pin device with a metal ball in the middle. When you put it upright, the 2 pins are connected together; when you tilt the switch, 2 pins will be disconnected.


**Schematic**

|sch_tilt|

When you put it upright, GP14 will get high; after tilting it, GP14 will get low.

The purpose of the 10K resistor is to keep the GP14 in a stable low state when the tilt switch is in a tilted state.

* :ref:`cpn_tilt`

**Wiring**

|wiring_tilt|

**Code**

.. note::

   * You can open the file ``2.6_tilt_it.ino`` under the path of ``kepler-kit-main/arduino/2.4_colorful_light``. 
   * Or copy this code into **Arduino IDE**.
   * For detailed tutorials, please refer to :ref:`open_run_code_ar`.
   * Or run this code directly in the `Arduino Web Editor <https://docs.arduino.cc/cloud/web-editor/tutorials/getting-started/getting-started-web-editor>`_.

    Don't forget to select the Raspberry Pi Pico W board and the correct port before clicking the Upload button.


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/0421b002-a697-4f22-a965-0e62e8dc3abf/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

    


After the program runs, when you tilt the breadboard (tilt switch), "The switch works!" will appear in the shell.