.. _py_button:

2.5 Reading Button Value
==============================================

These pins have both input and output functions, as indicated by their name GPIO (General-purpose input/output). Previously, we used the output function; in this chapter, we will use the input function to input the button value.

* :ref:`cpn_button`

**Required Components**

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
        - :ref:`cpn_pico_w`
        - 1
        - |link_picow_buy|
    *   - 2
        - Micro USB Cable
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Several
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|

**Schematic**

|sch_button|

As long as one side of the button pin is connected to 3.3v, and the other side pin is connected to GP14, then when the button is pressed, GP14 will be high. However, when the button is not pressed, GP14 is in a suspended state and may be high or low. In order to get a stable low level when the button is not pressed, GP14 needs to be reconnected to GND through a 10K pull-down resistor.


**Wiring**

|wiring_button|


.. Let's follow the direction of the circuit to build the circuit!

.. 1. Connect the 3V3 pin of Pico W to the positive power bus of the breadboard.
.. #. Insert the button into the breadboard and straddle the central dividing line.

.. note::
    A four-pin button is shaped like an H. Its left two pins or right two pins are connected, which means that when it crosses the central gap, it connects two half rows with the same row number. (For example, in my circuit, E23 and F23 are already connected, as are E25 and F25).

    Until the button is pressed, the left and right pins are independent of each other and current cannot flow from one side to the other.

.. #. Use a jumper wire to connect one of the button pins to the positive bus (mine is the pin on the upper right).
.. #. Connect the other pin (upper left or lower left) to GP14 with a jumper wire.
.. #. Use a 10K resistor to connect the pin on the upper left corner of the button and the negative bus.
.. #. Connect the negative power bus of the breadboard to Pico's GND.

**Code**

.. note::

    * Open the ``2.5_read_button_value.py`` file under the path of ``kepler-kit-main/micropython`` or copy this code into Thonny, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico)" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime
    button = machine.Pin(14, machine.Pin.IN)
    while True:
        if button.value() == 1:
            print("You pressed the button!")
            utime.sleep(1)

As soon as the code runs, the shell prints "You pressed the button!"

**Pull-up Working Mode**


The next part is the wiring and code when you use the button in the pull-up mode.

|sch_button_pullup|

|wiring_button_pullup|

The only difference you will see with the pull-down mode is that the 10K resistor is connected to 3.3V and the button is connected to GND, so that when the button is pressed, GP14 will get a low level, which is the opposite of the value obtained in pull-down mode.
So just change this code to ``if button.value() == 0:``.


Also see the reference here:  

* `machine.Pin <https://docs.micropython.org/en/latest/library/machine.Pin.html>`_