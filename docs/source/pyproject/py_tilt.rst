.. _py_tilt:


2.6 Tilt It！
==========================

|img_tilt|

The tilt switch is a 2-pin device with a metal ball in the middle. When the switch is upright, the two pins are connected; when it is tilted, the two pins are disconnected.

**Bill of Materials**

In this project, we need the following components. 

It's definitely convenient to buy a whole kit, here's the link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ITEMS IN THIS KIT
        - LINK
    *   - Kepler Kit	
        - 450+
        - |link_kepler_kit|


You can also buy them separately from the links below.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENT	
        - QUANTITY
        - LINK

    *   - 1
        - Raspberry Pi Pico W
        - 1
        - |link_picow_buy|
    *   - 2
        - Micro USB Cable
        - 1
        - 
    *   - 3
        - Breadboard
        - 1
        - |link_breadboard_buy|
    *   - 4
        - Wires
        - Several
        - |link_wires_buy|
    *   - 5
        - Resistor
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - Tilt Switch
        - 1
        - 

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