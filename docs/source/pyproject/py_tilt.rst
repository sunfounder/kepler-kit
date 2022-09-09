.. _py_tilt:


2.6 Tilt It！
==========================

|img_tilt|

The tilt switch is a 2-pin device with a metal ball in the middle. When the switch is upright, the two pins are connected; when it is tilted, the two pins are disconnected.


**Schematic**

|sch_tilt|

When you put it upright, GP14 will get high; after tilting it, GP14 will get low.

The purpose of the 10K resistor is to keep the GP14 in a stable low state when the tilt switch is in a tilted state.

* :ref:`cpn_tilt`

**Wiring**

|wiring_tilt|



**Code**

.. note::

    * Open the ``2.6_tilt_switch.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    button = machine.Pin(14, machine.Pin.IN)
    while True:
        if button.value() == 0:
            print("The switch works!")
            utime.sleep(1)

After the program runs, when you tilt the breadboard (tilt switch), "The switch works!" will appear in the shell.