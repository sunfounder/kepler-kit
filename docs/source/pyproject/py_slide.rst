.. _py_slide:

2.7 Toggle Left and Right
====================================

|img_slide|

The slide switch is a 3-pin device, with pin 2 (middle) being the common pin. When the switch is toggled to the left, the left two pins are connected together, and when toggled to the right, the right two pins are connected together. 


**Schematic**

|sch_slide|

GP14 will get a different level, when you toggle the slide switch to the right or left.

The purpose of the 10K resistor is to keep the GP14 low during toggling (not toggling to the far left and not toggling to the far right).

The 104 ceramic capacitor is used here to eliminate jitter.

* :ref:`cpn_slide`
* :ref:`cpn_cap`

**Wiring**

|wiring_slide|

**Code**

.. note::

    * Open the ``2.7_slide_switch.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

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


After the program runs, when you toggle the slide switch to the right, "The switch works!" will appear in the shell.